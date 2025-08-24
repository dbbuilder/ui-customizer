<!-- frontend/src/components/preview/ComponentPreview.vue -->
<template>
  <div class="h-full flex flex-col">
    <!-- Preview Controls -->
    <div class="flex-shrink-0 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-4 py-3">
      <div class="flex items-center justify-between">
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
          Component Preview
        </h3>
        <div v-if="generatedComponents.length > 0" class="text-sm text-gray-500 dark:text-gray-400">
          {{ generatedComponents.length }} component{{ generatedComponents.length > 1 ? 's' : '' }} generated
        </div>
      </div>
    </div>

    <!-- Preview Content -->
    <div class="flex-1 overflow-auto">
      <!-- Loading State -->
      <div v-if="loading" class="flex items-center justify-center h-full">
        <div class="text-center">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">
            Generating Components
          </h3>
          <p class="text-gray-500 dark:text-gray-400 max-w-sm">
            Please wait while we create your custom components...
          </p>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else-if="generatedComponents.length === 0" class="flex items-center justify-center h-full">
        <div class="text-center max-w-md">
          <div class="w-24 h-24 bg-gray-100 dark:bg-gray-700 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
            </svg>
          </div>
          <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">
            No Components Generated
          </h3>
          <p class="text-gray-500 dark:text-gray-400 mb-6">
            Customize your design system and click "Generate Preview" to create components.
          </p>
          <button
            @click="$emit('generatePreview')"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Generate Components
          </button>
        </div>
      </div>

      <!-- Component Grid -->
      <div v-else class="p-6">
        <div class="grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
          <div
            v-for="component in generatedComponents"
            :key="component.id"
            class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 p-6 hover:shadow-lg transition-shadow"
          >
            <!-- Component Header -->
            <div class="flex items-center justify-between mb-4">
              <div>
                <h4 class="text-lg font-medium text-gray-900 dark:text-white">
                  {{ component.name }}
                </h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">
                  {{ component.type }} - {{ component.variant }}
                </p>
              </div>
              <div class="flex space-x-1">
                <button
                  @click="viewCode(component)"
                  class="p-1 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200"
                  title="View code"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                  </svg>
                </button>
              </div>
            </div>

            <!-- Component Preview -->
            <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 mb-4">
              <div v-html="component.template" class="text-center"></div>
            </div>

            <!-- Component Info -->
            <div class="space-y-2">
              <div class="text-xs text-gray-500 dark:text-gray-400">
                Framework: {{ component.framework }}
              </div>
              <div class="text-xs text-gray-500 dark:text-gray-400">
                Accessibility: {{ component.accessibility_features.join(', ') }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { GeneratedComponent, Viewport, PreviewMode, DesignConfig } from '../../types'

interface Props {
  generatedComponents: GeneratedComponent[]
  currentViewport: Viewport
  previewMode: PreviewMode
  designConfig: DesignConfig
  loading: boolean
}

defineProps<Props>()

const emit = defineEmits<{
  componentUpdated: [component: GeneratedComponent]
  generatePreview: []
}>()

const viewCode = (component: GeneratedComponent) => {
  console.log('Viewing code for:', component.name)
  // TODO: Implement code modal
}
</script>