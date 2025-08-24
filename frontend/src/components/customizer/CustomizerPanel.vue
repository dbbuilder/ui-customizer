<!-- frontend/src/components/customizer/CustomizerPanel.vue -->
<template>
  <div class="h-full flex flex-col bg-white dark:bg-gray-800">
    <!-- Panel Header -->
    <div class="flex-shrink-0 px-6 py-4 border-b border-gray-200 dark:border-gray-700">
      <h2 class="text-lg font-semibold text-gray-900 dark:text-white">
        Customize Design
      </h2>
      <p class="mt-1 text-sm text-gray-600 dark:text-gray-400">
        Customize your design system and see live updates
      </p>
    </div>

    <!-- Scrollable Content -->
    <div class="flex-1 overflow-y-auto">
      <div class="p-6 space-y-8">
        
        <!-- Design Style Section -->
        <section>
          <h3 class="text-base font-medium text-gray-900 dark:text-white mb-4">
            Design Style
          </h3>
          
          <div class="grid grid-cols-2 gap-3">
            <button
              v-for="style in designStyles"
              :key="style.value"
              @click="updateStyle(style.value)"
              :class="[
                'p-3 rounded-lg border-2 text-left transition-all duration-200',
                modelValue.style === style.value
                  ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20'
                  : 'border-gray-200 dark:border-gray-600 hover:border-gray-300 dark:hover:border-gray-500'
              ]"
            >
              <div class="font-medium text-sm text-gray-900 dark:text-white">
                {{ style.label }}
              </div>
              <div class="text-xs text-gray-500 dark:text-gray-400 mt-1">
                {{ style.description }}
              </div>
            </button>
          </div>
        </section>

        <!-- Color Palette Section -->
        <section>
          <h3 class="text-base font-medium text-gray-900 dark:text-white mb-4">
            Color Palette
          </h3>
          
          <div class="space-y-4">
            <!-- Primary Color -->
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Primary Color
              </label>
              <div class="flex space-x-2">
                <input
                  type="text"
                  :value="modelValue.colorPalette.primary"
                  @input="updateColor('primary', $event.target.value)"
                  class="flex-1 block w-full rounded-md border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-sm focus:border-blue-500 focus:ring-blue-500 text-sm"
                  placeholder="#3B82F6"
                />
                <input
                  type="color"
                  :value="modelValue.colorPalette.primary"
                  @input="updateColor('primary', $event.target.value)"
                  class="w-10 h-9 rounded border border-gray-300 dark:border-gray-600 cursor-pointer"
                />
              </div>
            </div>
            
            <!-- Generate Palette Button -->
            <button
              @click="$emit('generatePreview')"
              :disabled="loading"
              class="w-full mt-4 inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-gradient-to-r from-purple-500 to-blue-500 hover:from-purple-600 hover:to-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
            >
              {{ loading ? 'Generating...' : 'Generate Palette' }}
            </button>
          </div>
        </section>

        <!-- Component Selection -->
        <section>
          <h3 class="text-base font-medium text-gray-900 dark:text-white mb-4">
            Components to Generate
          </h3>
          
          <div class="space-y-2">
            <label
              v-for="component in availableComponents"
              :key="component"
              class="flex items-center p-3 rounded-lg border border-gray-200 dark:border-gray-600 hover:border-gray-300 dark:hover:border-gray-500 cursor-pointer transition-colors"
            >
              <input
                type="checkbox"
                :value="component"
                v-model="selectedComponents"
                class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
              />
              <span class="ml-3 text-sm font-medium text-gray-900 dark:text-white">
                {{ component.charAt(0).toUpperCase() + component.slice(1) }}
              </span>
            </label>
          </div>
        </section>
      </div>
    </div>

    <!-- Fixed Bottom Action Bar -->
    <div class="flex-shrink-0 border-t border-gray-200 dark:border-gray-700 px-6 py-4">
      <button
        @click="$emit('generatePreview')"
        :disabled="loading || selectedComponents.length === 0"
        class="w-full inline-flex items-center justify-center px-4 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg hover:shadow-xl"
      >
        {{ loading ? 'Generating Preview...' : 'Generate Preview' }}
      </button>
      
      <p v-if="selectedComponents.length === 0" class="text-xs text-red-500 text-center mt-2">
        Select at least one component type to generate
      </p>
      <p v-else class="text-xs text-gray-500 dark:text-gray-400 text-center mt-2">
        {{ selectedComponents.length }} component{{ selectedComponents.length > 1 ? 's' : '' }} selected
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { DesignConfig } from '../../types'

interface Props {
  modelValue: DesignConfig
  availableComponents: string[]
  loading: boolean
}

const props = defineProps<Props>()

const emit = defineEmits<{
  'update:modelValue': [value: DesignConfig]
  'generatePreview': []
  'componentSelected': [componentType: string]
}>()

// Reactive state
const selectedComponents = ref<string[]>(['button', 'card'])

// Design style options
const designStyles = [
  { value: 'modern', label: 'Modern', description: 'Clean & contemporary' },
  { value: 'minimalist', label: 'Minimalist', description: 'Simple & refined' },
  { value: 'brutalist', label: 'Brutalist', description: 'Bold & geometric' },
  { value: 'glassmorphism', label: 'Glass', description: 'Translucent & layered' }
]

// Methods
const updateStyle = (style: string) => {
  const config = { ...props.modelValue }
  config.style = style as any
  emit('update:modelValue', config)
}

const updateColor = (colorType: string, value: string) => {
  const config = { ...props.modelValue }
  config.colorPalette[colorType as keyof typeof config.colorPalette] = value
  emit('update:modelValue', config)
}
</script>