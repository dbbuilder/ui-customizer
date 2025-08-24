<!-- frontend/src/components/common/NavHeader.vue -->
<template>
  <header class="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-4 py-3">
    <div class="flex items-center justify-between">
      <!-- Logo and Title -->
      <div class="flex items-center space-x-3">
        <div class="flex-shrink-0">
          <div class="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zm0 4a1 1 0 011-1h12a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1V8z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
        <div>
          <h1 class="text-xl font-bold text-gray-900 dark:text-white">
            UI Customizer
          </h1>
          <p class="text-xs text-gray-500 dark:text-gray-400">
            Dynamic Component Generator
          </p>
        </div>
      </div>

      <!-- Right Actions -->
      <div class="flex items-center space-x-3">
        <!-- Theme Toggle -->
        <div class="flex items-center space-x-1 bg-gray-100 dark:bg-gray-700 rounded-lg p-1">
          <button
            v-for="theme in themeOptions"
            :key="theme.value"
            @click="$emit('themeChanged', theme.value)"
            :class="[
              'p-1.5 rounded-md transition-colors',
              currentTheme === theme.value
                ? 'bg-white dark:bg-gray-600 text-gray-900 dark:text-white shadow-sm'
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
            ]"
            :title="`Switch to ${theme.label.toLowerCase()} theme`"
          >
            <component :is="theme.icon" class="w-4 h-4" />
          </button>
        </div>

        <!-- Save Button -->
        <button
          @click="$emit('saveProject')"
          class="inline-flex items-center px-3 py-1.5 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
          title="Save current project"
        >
          Save
        </button>

        <!-- Export Button -->
        <button
          @click="$emit('exportProject')"
          class="inline-flex items-center px-3 py-1.5 text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition-colors"
          title="Export generated components"
        >
          Export
        </button>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
interface Props {
  currentTheme: 'light' | 'dark' | 'system'
}

defineProps<Props>()

defineEmits<{
  themeChanged: [theme: 'light' | 'dark' | 'system']
  saveProject: []
  loadProject: []
  exportProject: []
}>()

// Mock theme options (you would import actual icons)
const themeOptions = [
  { value: 'light' as const, label: 'Light', icon: 'SunIcon' },
  { value: 'dark' as const, label: 'Dark', icon: 'MoonIcon' },
  { value: 'system' as const, label: 'System', icon: 'ComputerIcon' }
]
</script>