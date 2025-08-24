// frontend/src/stores/design.ts
/**
 * Pinia store for design system management
 */

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { DesignConfig, GeneratedComponent, ComponentGenerationResponse } from '../types'

export const useDesignStore = defineStore('design', () => {
  // State
  const designConfig = ref<DesignConfig>({
    style: 'modern',
    colorPalette: {
      primary: '#3B82F6',
      secondary: '#8B5CF6',
      accent: '#10B981',
      neutral: '#6B7280',
      background: '#FFFFFF',
      surface: '#F9FAFB'
    },
    typography: {
      fontFamily: 'Inter',
      headingFont: 'Inter',
      fontScale: 1.2,
      lineHeight: 1.6
    },
    spacing: {
      scale: 1,
      containerMaxWidth: '1200px',
      sectionPadding: '4rem'
    },
    borderRadius: {
      base: 0.5,
      button: 0.375,
      card: 0.75
    },
    animations: {
      duration: '200ms',
      easing: 'ease-in-out',
      enabled: true
    },
    accessibility: {
      highContrast: false,
      reducedMotion: false,
      focusVisible: true
    }
  })

  const generatedComponents = ref<GeneratedComponent[]>([])
  const isGenerating = ref(false)

  // Getters
  const componentCount = computed(() => generatedComponents.value.length)
  
  // Actions
  const updateDesignConfig = (path: string, value: any) => {
    const keys = path.split('.')
    let current: any = designConfig.value
    
    for (let i = 0; i < keys.length - 1; i++) {
      if (!current[keys[i]]) current[keys[i]] = {}
      current = current[keys[i]]
    }
    
    current[keys[keys.length - 1]] = value
  }

  const generateComponents = async (config: DesignConfig): Promise<ComponentGenerationResponse> => {
    isGenerating.value = true
    
    try {
      // Mock API call for now
      const response: ComponentGenerationResponse = {
        success: true,
        message: 'Components generated successfully',
        components: [
          {
            id: '1',
            name: 'PrimaryButton',
            type: 'button',
            variant: 'primary',
            framework: 'vue',
            template: '<button class="btn-primary">Click me</button>',
            styles: { main: '.btn-primary { background: #3B82F6; }' },
            props: { size: 'md', variant: 'primary' },
            usage_example: '<PrimaryButton>Click me</PrimaryButton>',
            accessibility_features: ['keyboard-navigation', 'aria-labels'],
            created_at: new Date().toISOString()
          }
        ],
        design_tokens: config,
        generation_time: 0.5,
        total_components: 1
      }
      
      generatedComponents.value = response.components
      return response
      
    } catch (error) {
      console.error('Error generating components:', error)
      throw error
    } finally {
      isGenerating.value = false
    }
  }

  const exportCode = async (components: GeneratedComponent[], format: 'vue' | 'react') => {
    // Mock export functionality
    return {
      success: true,
      files: {
        'Button.vue': '<template><button>Mock Button</button></template>'
      }
    }
  }

  return {
    designConfig,
    generatedComponents,
    isGenerating,
    componentCount,
    updateDesignConfig,
    generateComponents,
    exportCode
  }
})