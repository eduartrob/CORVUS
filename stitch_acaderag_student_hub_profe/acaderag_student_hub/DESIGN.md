---
name: AcadeRAG Student Hub
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#ddb7ff'
  on-secondary: '#490080'
  secondary-container: '#6f00be'
  on-secondary-container: '#d6a9ff'
  tertiary: '#4fdbc8'
  on-tertiary: '#003731'
  tertiary-container: '#00a392'
  on-tertiary-container: '#00302a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#f0dbff'
  secondary-fixed-dim: '#ddb7ff'
  on-secondary-fixed: '#2c0051'
  on-secondary-fixed-variant: '#6900b3'
  tertiary-fixed: '#71f8e4'
  tertiary-fixed-dim: '#4fdbc8'
  on-tertiary-fixed: '#00201c'
  on-tertiary-fixed-variant: '#005048'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  gutter: 1.5rem
  margin: 2rem
  container-max: 1280px
---

## Brand & Style
The design system is built for a high-fidelity educational SaaS environment that prioritizes deep focus, AI-driven efficiency, and a premium developer-grade aesthetic. It draws heavy inspiration from modern, high-performance tools like Vercel and Linear, utilizing a dark-first philosophy to reduce eye strain during long study sessions.

The style is **Minimalist Glassmorphism**. It combines the structural rigor of a professional dashboard with the ethereal quality of semi-transparent surfaces and vibrant, glowing accents. This creates a sense of "intellectual space" where information feels layered rather than flat, guiding the student's attention through subtle depth and light.

## Colors
The palette is rooted in **Dark Slate**, providing a sophisticated, low-fatigue backdrop. 
- **Primary (Indigo #6366f1):** Used for primary actions and focused states.
- **Secondary (Purple #a855f7):** Reserved for AI-driven features, insights, and premium "pro" indicators.
- **Gradients:** Actionable elements often utilize a linear gradient from Indigo to Purple to signify energy and motion.
- **Surfaces:** Backgrounds use Slate-900. Component surfaces use Slate-800 with 70% opacity and a `20px` backdrop-blur to create the glassmorphism effect.
- **Accents:** Vibrant Teal (#14b8a6) is used sparingly for success states and completion markers.

## Typography
The system relies on **Inter** for its incredible readability and neutral, modern character. For technical or meta-data elements (labels, tags, AI status), **Geist** is introduced to provide a "developer-tool" feel that emphasizes precision.

Hierarchy is established through weight and optical sizing. Headlines use tighter letter-spacing and heavier weights to feel impactful against the dark background. Body text maintains a generous line height (1.6) to ensure long-form educational content is easy to digest. High contrast (White/Slate-100 on Slate-900) is maintained for all functional text.

## Layout & Spacing
This design system uses a **12-column fluid grid** for desktop, transitioning to a **4-column grid** for mobile. 

The spacing philosophy follows a strict 4px/8px baseline rhythm. 
- **Desktop:** 24px (1.5rem) gutters with 32px (2rem) side margins.
- **Mobile:** 16px (1rem) gutters with 16px (1rem) side margins.

Layouts should favor vertical stack patterns for information-heavy pages (like document readers) and grid-based card layouts for dashboard overviews. Use "Safe Areas" around the central content container to maintain the minimalist aesthetic.

## Elevation & Depth
Depth is created through transparency and "inner glow" rather than heavy drop shadows.

1.  **Level 0 (Base):** Slate-900 (Solid).
2.  **Level 1 (Cards/Sidebar):** Slate-800 at 70% opacity + 20px Backdrop Blur + 1px Border (Slate-700/50).
3.  **Level 2 (Modals/Popovers):** Slate-800 at 90% opacity + 40px Backdrop Blur + 1px Border (Slate-600/50) + Soft Shadow (0 20px 25px -5px rgba(0,0,0,0.5)).
4.  **Active State:** Elements in focus should receive a subtle 1px "Indigo" glow (box-shadow: 0 0 15px rgba(99, 102, 241, 0.3)).

## Shapes
The shape language is contemporary and "soft-tech."
- **Standard UI (Buttons, Inputs):** 0.5rem (8px) radius.
- **Container UI (Cards, Sections):** 1rem (16px) radius.
- **Large UI (Modals, Feature Hero):** 1.5rem (24px) radius.

All borders should be kept thin (1px) and use semi-transparent colors to blend into the glass effect.

## Components
- **Buttons:** Primary buttons use an Indigo-to-Purple gradient with white text. Secondary buttons are "ghost" style with a Slate-700 border and subtle hover fill.
- **Chips/Badges:** Use Geist font, 12px, semi-transparent backgrounds with high-contrast text. For AI-generated tags, use a purple tint.
- **Input Fields:** Slate-800 background, 1px Slate-700 border. On focus, the border transitions to Indigo with a subtle outer glow.
- **Cards:** The hallmark component. Must have `backdrop-filter: blur(20px)`, a 1px border at 50% opacity, and rounded-2xl corners.
- **AI Hub Component:** A dedicated floating action area or sidebar section characterized by a mesh-gradient border and Geist-font typography to distinguish AI suggestions from static content.
- **Checkboxes & Radios:** Sharp, high-contrast markers. Checked states use the Indigo primary color.