#!/usr/bin/env python3
"""Build tokens.css and tailwind.config.js from tokens.json (stdlib only).

tokens.json is the single source of truth. Never edit the generated files by hand.

  python design/tokens/build_tokens.py          # build + contrast check
  python design/tokens/build_tokens.py --check  # only verify that generated files are current + contrast

Contrast check: every text/background pair in CONTRAST_PAIRS must reach its WCAG 2.x
minimum in both light and dark mode, otherwise the script exits 1.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "tokens.json"
CSS_OUT = HERE / "tokens.css"
TW_OUT = HERE / "tailwind.config.js"
HEADER = "Generated from tokens.json by build_tokens.py — do not edit by hand."

# (foreground, background, minimum ratio). 4.5 = normal text, 3.0 = UI component/border.
CONTRAST_PAIRS = [
    ("text", "bg", 4.5), ("text", "surface", 4.5), ("text-body", "surface", 4.5),
    ("text-muted", "surface", 4.5), ("text-muted", "bg", 4.5),
    ("on-primary", "primary", 4.5), ("primary", "surface", 4.5), ("primary", "bg", 4.5),
    ("on-primary-subtle", "primary-subtle", 4.5), ("secondary", "surface", 4.5),
    ("on-secondary-subtle", "secondary-subtle", 4.5),
    ("success", "surface", 4.5), ("on-success-subtle", "success-subtle", 4.5),
    ("warning", "surface", 4.5), ("on-warning-subtle", "warning-subtle", 4.5),
    ("error", "surface", 4.5), ("on-error-subtle", "error-subtle", 4.5),
    ("info", "surface", 4.5), ("on-info-subtle", "info-subtle", 4.5),
    ("border-input", "surface", 3.0), ("focus", "surface", 3.0), ("focus", "bg", 3.0),
]
WHITE_ON = [("error-fill", 4.5)]  # white text on these fills
# Extra pairs for the app-v2 palette (navy sidebar).
APP_PAIRS = [
    ("sidebar-text", "sidebar", 4.5), ("sidebar-text-muted", "sidebar", 4.5),
    ("on-sidebar-active", "sidebar-active", 4.5),
]
PALETTES = ("app-v2",)  # extra light palettes, switched with <html data-palette="...">
# Dark variant of an extra palette: <html data-palette="app-v2" data-theme="dark">.
DARK_PALETTES = {"app-v3-dark": "app-v2"}
# Buttons in app-v3-dark use "action" (deep teal + white); "primary" there is the light accent for text/icons.
DARK_APP_PAIRS = [("on-action", "action", 4.5), ("on-action", "action-hover", 4.5)]


def load() -> dict:
    return json.loads(SRC.read_text(encoding="utf-8"))


def lookup(tokens: dict, path: str):
    node = tokens
    for part in path.split("."):
        node = node[part]
    return node["$value"]


def resolve(tokens: dict, value):
    if isinstance(value, str):
        m = re.fullmatch(r"\{([^}]+)\}", value)
        if m:
            return resolve(tokens, lookup(tokens, m.group(1)))
    return value


def leaves(node: dict, prefix: tuple[str, ...] = ()):
    for key, child in node.items():
        if key.startswith("$") or not isinstance(child, dict):
            continue
        if "$value" in child:
            yield prefix + (key,), child
        else:
            yield from leaves(child, prefix + (key,))


def var_name(path: tuple[str, ...]) -> str:
    """camelCase segments become kebab-case: ("font", "lineHeight", "body") -> font-line-height-body."""
    return "-".join(re.sub(r"(?<!^)([A-Z])", r"-\1", p).lower() for p in path)


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def css_value(path: tuple[str, ...], value) -> str:
    if isinstance(value, list):
        if path[0] == "motion":
            return "cubic-bezier(" + ", ".join(str(v) for v in value) + ")"
        return ", ".join(f'"{v}"' if " " in v else v for v in value)
    return str(value)


def build_css(tokens: dict) -> str:
    out = [f"/* {HEADER} */", "", ":root {"]
    for path, leaf in leaves(tokens):
        if path[0] == "semantic":
            continue
        out.append(f"  --{var_name(path)}: {css_value(path, resolve(tokens, leaf['$value']))};")
    out.append("")
    out.append("  /* semantic: light (default) */")
    for path, leaf in leaves(tokens["semantic"]["light"]):
        out.append(f"  --color-{'-'.join(path)}: {resolve(tokens, leaf['$value'])};")
    out.append("}")
    dark = [f"  --color-{'-'.join(p)}: {resolve(tokens, l['$value'])};" for p, l in leaves(tokens["semantic"]["dark"])]
    for name in PALETTES:
        out += ["", f'/* palette {name}: <html data-palette="{name}"> */', f':root[data-palette="{name}"] {{']
        out += [f"  --color-{'-'.join(p)}: {resolve(tokens, l['$value'])};" for p, l in leaves(tokens["semantic"][name])]
        out.append("}")
    for name, base in DARK_PALETTES.items():
        out += ["", f'/* palette {name}: <html data-palette="{base}" data-theme="dark"> */',
                f':root[data-palette="{base}"][data-theme="dark"] {{']
        out += [f"  --color-{'-'.join(p)}: {resolve(tokens, l['$value'])};" for p, l in leaves(tokens["semantic"][name])]
        out.append("}")
    out += ["", "@media (prefers-color-scheme: dark) {", '  :root:not([data-theme="light"]):not([data-palette]) {']
    out += ["  " + line for line in dark] + ["  }", "}", "", ':root[data-theme="dark"] {'] + dark + ["}", ""]
    out += [
        "@media (prefers-reduced-motion: reduce) {",
        "  :root {",
        "    --motion-duration-instant: 0ms; --motion-duration-fast: 0ms; --motion-duration-base: 0ms;",
        "    --motion-duration-slow: 0ms; --motion-duration-shimmer: 0ms;",
        "  }",
        "}",
        "",
    ]
    return "\n".join(out)


def scale(tokens: dict, group: tuple[str, ...], var_prefix: str) -> dict:
    node = tokens
    for g in group:
        node = node[g]
    return {"-".join(p): f"var(--{var_prefix}-{var_name(p)})" for p, _ in leaves(node)}


def build_tailwind(tokens: dict) -> str:
    colors = {name: scale(tokens, ("color", name), f"color-{name}") for name in tokens["color"] if not name.startswith("$")}
    # Role colors switch with light/dark via CSS variables:
    #   bg-primary / text-success  -> role color (DEFAULT), bg-primary-600 -> raw palette step
    #   bg-ui-surface / text-ui-text-muted / border-ui-border-input -> other roles
    roles = {"-".join(p): f"var(--color-{'-'.join(p)})" for p, _ in leaves(tokens["semantic"]["light"])}
    for name in (*PALETTES, *DARK_PALETTES):
        roles.update({"-".join(p): f"var(--color-{'-'.join(p)})" for p, _ in leaves(tokens["semantic"][name])})
    for name in ("primary", "secondary", "success", "warning", "error", "info"):
        colors[name] = {"DEFAULT": roles[name], **colors[name]}
    colors["ui"] = roles
    theme = {
        "colors": {**colors, "transparent": "transparent", "current": "currentColor"},
        "fontFamily": {k: [f"var(--font-family-{k})"] for k in ("heading", "body", "mono")},
        "fontSize": scale(tokens, ("font", "size"), "font-size"),
        "fontWeight": scale(tokens, ("font", "weight"), "font-weight"),
        "lineHeight": scale(tokens, ("font", "lineHeight"), "font-line-height"),
        "spacing": {**scale(tokens, ("spacing",), "spacing"), "px": "1px"},
        "borderRadius": scale(tokens, ("radius",), "radius"),
        "boxShadow": scale(tokens, ("shadow",), "shadow"),
        "zIndex": scale(tokens, ("zIndex",), "z-index"),
        "screens": {k: resolve(tokens, v["$value"]) for (k,), v in leaves(tokens["breakpoint"])},
        "extend": {
            "maxWidth": scale(tokens, ("container",), "container"),
            "minHeight": {"tap": "var(--size-tap-min)"},
            "minWidth": {"tap": "var(--size-tap-min)"},
            "transitionDuration": scale(tokens, ("motion", "duration"), "motion-duration"),
            "transitionTimingFunction": {"standard": "var(--motion-easing-standard)"},
        },
    }
    body = json.dumps(theme, indent=2, ensure_ascii=False)
    return (
        f"// {HEADER}\n"
        "// Values point to CSS variables in tokens.css, so light/dark switching needs no rebuild.\n"
        "// Usage: import './design/tokens/tokens.css' once, then extend this config.\n"
        "/** @type {import('tailwindcss').Config} */\n"
        "module.exports = {\n"
        "  darkMode: ['class', '[data-theme=\"dark\"]'],\n"
        f"  theme: {body.replace(chr(10), chr(10) + '  ')},\n"
        "};\n"
    )


def check_contrast(tokens: dict) -> list[str]:
    problems = []
    for mode in ("light", "dark", *PALETTES, *DARK_PALETTES):
        sem = {"-".join(p): resolve(tokens, l["$value"]) for p, l in leaves(tokens["semantic"][mode])}
        extra = APP_PAIRS if mode in PALETTES else APP_PAIRS + DARK_APP_PAIRS if mode in DARK_PALETTES else []
        for fg, bg, minimum in CONTRAST_PAIRS + extra:
            r = ratio(sem[fg], sem[bg])
            if r < minimum:
                problems.append(f"{mode}: {fg} on {bg} = {r:.2f} < {minimum}")
        for fill, minimum in WHITE_ON:
            r = ratio("#FFFFFF", sem[fill])
            if r < minimum:
                problems.append(f"{mode}: white on {fill} = {r:.2f} < {minimum}")
    return problems


def main() -> int:
    tokens = load()
    css, tw = build_css(tokens), build_tailwind(tokens)
    problems = check_contrast(tokens)
    if "--check" in sys.argv[1:]:
        for path, content in ((CSS_OUT, css), (TW_OUT, tw)):
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                problems.append(f"{path.name} is out of date: run python design/tokens/build_tokens.py")
    else:
        CSS_OUT.write_text(css, encoding="utf-8")
        TW_OUT.write_text(tw, encoding="utf-8")
        print(f"wrote {CSS_OUT.name}, {TW_OUT.name}")
    if problems:
        print("FAIL")
        for p in problems:
            print(f"  - {p}")
        return 1
    n = (len(CONTRAST_PAIRS) + len(WHITE_ON)) * 2 + (len(CONTRAST_PAIRS) + len(APP_PAIRS) + len(WHITE_ON)) * len(PALETTES)
    n += (len(CONTRAST_PAIRS) + len(APP_PAIRS) + len(DARK_APP_PAIRS) + len(WHITE_ON)) * len(DARK_PALETTES)
    print(f"PASS — {n} contrast pairs meet WCAG AA (light + dark + {', '.join((*PALETTES, *DARK_PALETTES))})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
