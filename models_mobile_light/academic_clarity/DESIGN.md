---
name: Academic Clarity
colors:
  surface: '#f8f9ff'
  surface-dim: '#ccdbf3'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d5e3fc'
  on-surface: '#0d1c2e'
  on-surface-variant: '#444653'
  inverse-surface: '#233144'
  inverse-on-surface: '#eaf1ff'
  outline: '#757684'
  outline-variant: '#c4c5d5'
  surface-tint: '#3755c3'
  primary: '#00288e'
  on-primary: '#ffffff'
  primary-container: '#1e40af'
  on-primary-container: '#a8b8ff'
  inverse-primary: '#b8c4ff'
  secondary: '#795900'
  on-secondary: '#ffffff'
  secondary-container: '#ffc329'
  on-secondary-container: '#6f5100'
  tertiary: '#323537'
  on-tertiary: '#ffffff'
  tertiary-container: '#484c4e'
  on-tertiary-container: '#b9bcbe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b8c4ff'
  on-primary-fixed: '#001453'
  on-primary-fixed-variant: '#173bab'
  secondary-fixed: '#ffdf9f'
  secondary-fixed-dim: '#f9bd22'
  on-secondary-fixed: '#261a00'
  on-secondary-fixed-variant: '#5c4300'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f8f9ff'
  on-background: '#0d1c2e'
  surface-variant: '#d5e3fc'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 40px
  margin-mobile: 16px
---

## Brand & Style

This design system transitions from high-contrast premium aesthetics to a sophisticated, light-mode educational environment. The brand personality is authoritative yet accessible, mimicking the clarity of modern academic journals and high-end learning management systems. 

The design style follows a **Corporate / Modern** approach with a strong emphasis on **Minimalism**. It prioritizes heavy white space (Paper White) to reduce cognitive load during intensive research and learning tasks. Visual hierarchy is established through precise typography and subtle tonal shifts rather than aggressive decoration, ensuring the user's focus remains entirely on the content and knowledge retrieval.

## Colors

The palette is anchored by **University Blue** (#1e40af), used for primary actions, navigational headers, and brand identification. This color provides a sense of stability and institutional trust. **Knowledge Gold** (#fbbf24) acts as a high-visibility accent for highlights, progress indicators, and "aha" moments within the UI, used sparingly to maintain professionalism.

The background architecture utilizes **Paper White** (#f8fafc) and pure white (#ffffff) to create a clean, layered canvas. Text employs a range of Slate neutrals, with #1e293b for primary headings to ensure maximum legibility and #475569 for body text to reduce eye strain during long reading sessions.

## Typography

The design system exclusively uses **Inter** to leverage its systematic, utilitarian nature. The scale is optimized for information density and readability. 

Headlines use semi-bold and bold weights with tighter letter-spacing to create a strong visual anchor. Body text is set with generous line-height (1.5x) to facilitate "deep reading" of academic papers and RAG-generated summaries. Small labels use a slightly increased letter-spacing and medium weight to maintain clarity at reduced scales. On mobile devices, headline sizes scale down to prevent excessive word-breaking while maintaining the 8px baseline rhythm.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model for desktop to ensure content remains readable and lines of text do not become exhaustingly wide. A 12-column grid is standard, with content centered in a 1280px container.

Spacing follows a strict 8px linear scale. For educational content, we prioritize vertical "breathing room" between sections (e.g., 48px or 64px) to separate distinct ideas. On mobile, the grid collapses to a single column with 16px side margins. Gutters are kept at a consistent 24px to provide clear visual separation between sidebar navigation and the primary reading area.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layers** and extremely **Ambient Shadows**. Instead of heavy shadows, we use 1px borders in a soft neutral (#e2e8f0) to define boundaries.

- **Level 0 (Surface):** The main background using Paper White.
- **Level 1 (Card/Container):** Pure white surfaces with a very soft, diffused shadow (0px 4px 12px rgba(0,0,0,0.03)) to lift content slightly.
- **Level 2 (Interaction):** Active elements or modals use a more pronounced but still subtle shadow (0px 10px 25px rgba(0,0,0,0.08)).

This approach maintains the "clean and organized" requirement without the clutter of traditional skeuomorphism.

## Shapes

The shape language is defined by the **Rounded** setting, specifically utilizing **rounded-xl** (1.5rem / 24px) for major containers and cards to create a modern, friendly, and premium feel. 

Smaller components like buttons and input fields utilize the standard **rounded-lg** (1rem / 16px) to maintain a cohesive language that feels soft and approachable, contrasting with the structured, "serious" academic nature of the typography and blue color palette.

## Components

- **Buttons:** Primary buttons use University Blue with white text and a rounded-lg radius. Secondary buttons use a subtle ghost style with a 1px border.
- **Cards:** White backgrounds, rounded-xl corners, and 1px #e2e8f0 borders. No heavy shadows.
- **Input Fields:** Soft grey backgrounds (#f1f5f9) that transition to white on focus with a University Blue 2px border.
- **Chips/Tags:** Used for academic subjects or metadata. These use a very light tint of the primary color (University Blue at 10% opacity) with dark blue text.
- **Lists:** Clean, unbordered rows with 16px vertical padding, separated by a 1px horizontal hairline.
- **Progress Bars:** Knowledge Gold is used for the fill color to represent the "accumulation of knowledge" or completion.
- **Source Citations:** Specific component for RAG results; small, rounded-md boxes with monospaced reference numbers, appearing in a sidebar or as inline tooltips.