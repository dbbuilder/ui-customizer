// frontend/src/types/index.ts
/**
 * Type definitions for the UI Customizer Tool
 */

export type Theme = 'light' | 'dark' | 'system'
export type Viewport = 'mobile' | 'tablet' | 'desktop' | 'wide'
export type PreviewMode = 'interactive' | 'static' | 'accessibility'
export type ExportFormat = 'vue' | 'react'

export type DesignStyle = 
  | 'modern' 
  | 'minimalist' 
  | 'brutalist' 
  | 'glassmorphism' 
  | 'neumorphism' 
  | 'retro' 
  | 'organic' 
  | 'geometric'

export type ComponentType = 
  | 'button' 
  | 'card' 
  | 'form' 
  | 'input' 
  | 'select' 
  | 'checkbox' 
  | 'radio' 
  | 'toggle' 
  | 'modal' 
  | 'dropdown' 
  | 'navigation' 
  | 'breadcrumb' 
  | 'tab' 
  | 'accordion' 
  | 'table' 
  | 'list' 
  | 'avatar' 
  | 'badge' 
  | 'alert' 
  | 'tooltip'

// Color System
export interface ColorPalette {
  primary: string
  secondary: string
  accent: string
  neutral: string
  background: string
  surface: string
  success?: string
  warning?: string
  error?: string
  info?: string
}

// Typography System
export interface Typography {
  fontFamily: string
  headingFont: string
  fontScale: number
  lineHeight: number
}

// Spacing System
export interface Spacing {
  scale: number
  containerMaxWidth: string
  sectionPadding: string
}

// Border Radius System
export interface BorderRadius {
  base: number
  button: number
  card: number
}

// Animation System
export interface Animations {
  duration: string
  easing: string
  enabled: boolean
}

// Accessibility Settings
export interface Accessibility {
  highContrast: boolean
  reducedMotion: boolean
  focusVisible: boolean
}

// Complete Design Configuration
export interface DesignConfig {
  style: DesignStyle
  colorPalette: ColorPalette
  typography: Typography
  spacing: Spacing
  borderRadius: BorderRadius
  animations: Animations
  accessibility: Accessibility
}

// Generated Component
export interface GeneratedComponent {
  id: string
  name: string
  type: ComponentType
  variant: string
  framework: ExportFormat
  template: string
  styles: Record<string, string>
  props: Record<string, any>
  usage_example: string
  accessibility_features: string[]
  created_at: string
}

// API Response Types
export interface ComponentGenerationResponse {
  success: boolean
  message: string
  components: GeneratedComponent[]
  design_tokens: Record<string, any>
  generation_time: number
  total_components: number
}