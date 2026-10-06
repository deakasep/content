// Generated from tokens.json by build_tokens.py — do not edit by hand.
// Values point to CSS variables in tokens.css, so light/dark switching needs no rebuild.
// Usage: import './design/tokens/tokens.css' once, then extend this config.
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    "colors": {
      "primary": {
        "DEFAULT": "var(--color-primary)",
        "50": "var(--color-primary-50)",
        "100": "var(--color-primary-100)",
        "200": "var(--color-primary-200)",
        "300": "var(--color-primary-300)",
        "400": "var(--color-primary-400)",
        "500": "var(--color-primary-500)",
        "600": "var(--color-primary-600)",
        "700": "var(--color-primary-700)",
        "800": "var(--color-primary-800)",
        "900": "var(--color-primary-900)"
      },
      "secondary": {
        "DEFAULT": "var(--color-secondary)",
        "50": "var(--color-secondary-50)",
        "100": "var(--color-secondary-100)",
        "400": "var(--color-secondary-400)",
        "600": "var(--color-secondary-600)",
        "700": "var(--color-secondary-700)"
      },
      "neutral": {
        "0": "var(--color-neutral-0)",
        "50": "var(--color-neutral-50)",
        "100": "var(--color-neutral-100)",
        "200": "var(--color-neutral-200)",
        "300": "var(--color-neutral-300)",
        "400": "var(--color-neutral-400)",
        "500": "var(--color-neutral-500)",
        "550": "var(--color-neutral-550)",
        "600": "var(--color-neutral-600)",
        "700": "var(--color-neutral-700)",
        "800": "var(--color-neutral-800)",
        "850": "var(--color-neutral-850)",
        "900": "var(--color-neutral-900)",
        "950": "var(--color-neutral-950)"
      },
      "success": {
        "DEFAULT": "var(--color-success)",
        "50": "var(--color-success-50)",
        "400": "var(--color-success-400)",
        "700": "var(--color-success-700)",
        "800": "var(--color-success-800)"
      },
      "warning": {
        "DEFAULT": "var(--color-warning)",
        "50": "var(--color-warning-50)",
        "200": "var(--color-warning-200)",
        "400": "var(--color-warning-400)",
        "700": "var(--color-warning-700)",
        "800": "var(--color-warning-800)"
      },
      "error": {
        "DEFAULT": "var(--color-error)",
        "50": "var(--color-error-50)",
        "200": "var(--color-error-200)",
        "400": "var(--color-error-400)",
        "600": "var(--color-error-600)",
        "700": "var(--color-error-700)",
        "800": "var(--color-error-800)"
      },
      "info": {
        "DEFAULT": "var(--color-info)",
        "50": "var(--color-info-50)",
        "400": "var(--color-info-400)",
        "700": "var(--color-info-700)",
        "800": "var(--color-info-800)"
      },
      "chart": {
        "1": "var(--color-chart-1)",
        "2": "var(--color-chart-2)",
        "3": "var(--color-chart-3)",
        "4": "var(--color-chart-4)",
        "5": "var(--color-chart-5)"
      },
      "ui": {
        "bg": "var(--color-bg)",
        "surface": "var(--color-surface)",
        "surface-raised": "var(--color-surface-raised)",
        "text": "var(--color-text)",
        "text-body": "var(--color-text-body)",
        "text-muted": "var(--color-text-muted)",
        "border": "var(--color-border)",
        "border-input": "var(--color-border-input)",
        "primary": "var(--color-primary)",
        "primary-hover": "var(--color-primary-hover)",
        "on-primary": "var(--color-on-primary)",
        "primary-subtle": "var(--color-primary-subtle)",
        "on-primary-subtle": "var(--color-on-primary-subtle)",
        "secondary": "var(--color-secondary)",
        "secondary-subtle": "var(--color-secondary-subtle)",
        "on-secondary-subtle": "var(--color-on-secondary-subtle)",
        "success": "var(--color-success)",
        "success-subtle": "var(--color-success-subtle)",
        "on-success-subtle": "var(--color-on-success-subtle)",
        "warning": "var(--color-warning)",
        "warning-subtle": "var(--color-warning-subtle)",
        "on-warning-subtle": "var(--color-on-warning-subtle)",
        "error": "var(--color-error)",
        "error-fill": "var(--color-error-fill)",
        "error-subtle": "var(--color-error-subtle)",
        "on-error-subtle": "var(--color-on-error-subtle)",
        "info": "var(--color-info)",
        "info-subtle": "var(--color-info-subtle)",
        "on-info-subtle": "var(--color-on-info-subtle)",
        "focus": "var(--color-focus)"
      },
      "transparent": "transparent",
      "current": "currentColor"
    },
    "fontFamily": {
      "heading": [
        "var(--font-family-heading)"
      ],
      "body": [
        "var(--font-family-body)"
      ],
      "mono": [
        "var(--font-family-mono)"
      ]
    },
    "fontSize": {
      "display": "var(--font-size-display)",
      "h2": "var(--font-size-h2)",
      "h3": "var(--font-size-h3)",
      "h4": "var(--font-size-h4)",
      "h5": "var(--font-size-h5)",
      "h6": "var(--font-size-h6)",
      "body": "var(--font-size-body)",
      "small": "var(--font-size-small)",
      "tiny": "var(--font-size-tiny)"
    },
    "fontWeight": {
      "regular": "var(--font-weight-regular)",
      "medium": "var(--font-weight-medium)",
      "semibold": "var(--font-weight-semibold)",
      "bold": "var(--font-weight-bold)"
    },
    "lineHeight": {
      "tight": "var(--font-line-height-tight)",
      "snug": "var(--font-line-height-snug)",
      "small": "var(--font-line-height-small)",
      "body": "var(--font-line-height-body)"
    },
    "spacing": {
      "0": "var(--spacing-0)",
      "1": "var(--spacing-1)",
      "2": "var(--spacing-2)",
      "3": "var(--spacing-3)",
      "4": "var(--spacing-4)",
      "5": "var(--spacing-5)",
      "6": "var(--spacing-6)",
      "8": "var(--spacing-8)",
      "12": "var(--spacing-12)",
      "16": "var(--spacing-16)",
      "24": "var(--spacing-24)",
      "px": "1px"
    },
    "borderRadius": {
      "none": "var(--radius-none)",
      "sm": "var(--radius-sm)",
      "md": "var(--radius-md)",
      "lg": "var(--radius-lg)",
      "xl": "var(--radius-xl)",
      "full": "var(--radius-full)"
    },
    "boxShadow": {
      "sm": "var(--shadow-sm)",
      "md": "var(--shadow-md)",
      "lg": "var(--shadow-lg)"
    },
    "zIndex": {
      "dropdown": "var(--z-index-dropdown)",
      "sticky": "var(--z-index-sticky)",
      "modal": "var(--z-index-modal)",
      "toast": "var(--z-index-toast)"
    },
    "screens": {
      "sm": "600px",
      "md": "768px",
      "lg": "1024px",
      "xl": "1440px"
    },
    "extend": {
      "maxWidth": {
        "form": "var(--container-form)",
        "tablet": "var(--container-tablet)",
        "desktop": "var(--container-desktop)",
        "wide": "var(--container-wide)",
        "prose": "var(--container-prose)"
      },
      "minHeight": {
        "tap": "var(--size-tap-min)"
      },
      "minWidth": {
        "tap": "var(--size-tap-min)"
      },
      "transitionDuration": {
        "instant": "var(--motion-duration-instant)",
        "fast": "var(--motion-duration-fast)",
        "base": "var(--motion-duration-base)",
        "slow": "var(--motion-duration-slow)",
        "shimmer": "var(--motion-duration-shimmer)"
      },
      "transitionTimingFunction": {
        "standard": "var(--motion-easing-standard)"
      }
    }
  },
};
