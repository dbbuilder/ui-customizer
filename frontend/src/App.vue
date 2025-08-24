<!-- frontend/src/App.vue -->
<template>
  <div id="app" class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <!-- Navigation Header -->
    <NavHeader 
      :current-theme="currentTheme"
      @theme-changed="handleThemeChange"
      @save-project="handleSaveProject"
      @load-project="handleLoadProject"
    />
    
    <!-- Main Application Layout -->
    <div class="flex flex-1 overflow-hidden">
      <!-- Left Sidebar - Customization Controls -->
      <aside 
        class="w-80 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 overflow-y-auto"
        :class="{ 'hidden lg:block': !sidebarOpen }"
      >
        <CustomizerPanel
          v-model:design-config="designConfig"
          :available-components="availableComponents"
          :loading="isGenerating"
          @generate-preview="generatePreview"
          @component-selected="handleComponentSelection"
        />
      </aside>
      
      <!-- Main Content Area -->
      <main class="flex-1 flex flex-col overflow-hidden">
        <!-- Preview Area -->
        <div class="flex-1 p-6 overflow-auto">
          <ComponentPreview
            :generated-components="generatedComponents"
            :current-viewport="currentViewport"
            :preview-mode="previewMode"
            :design-config="designConfig"
            :loading="isGenerating"
            @component-updated="handleComponentUpdate"
          />
        </div>
      </main>
    </div>
    
    <!-- Loading Overlay -->
    <div v-if="isGenerating" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-8 max-w-sm w-full mx-4">
        <div class="text-center">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-2">
            Generating Components
          </h3>
          <p class="text-gray-500 dark:text-gray-400">
            {{ loadingMessage || 'Please wait while we create your custom components...' }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed, watch } from 'vue'
import { useDesignStore } from './stores/design'
import { useNotificationStore } from './stores/notifications'
import { useErrorHandler } from './composables/useErrorHandler'
import { useLocalStorage } from '@vueuse/core'

// Component imports
import NavHeader from './components/common/NavHeader.vue'
import CustomizerPanel from './components/customizer/CustomizerPanel.vue'
import ComponentPreview from './components/preview/ComponentPreview.vue'

// Types
import type { 
  DesignConfig, 
  GeneratedComponent, 
  Viewport, 
  PreviewMode,
  ExportFormat,
  Theme,
  ComponentType
} from './types'

// Stores and composables
const designStore = useDesignStore()
const notificationStore = useNotificationStore()
const { handleError, currentError } = useErrorHandler()

// Reactive state
const sidebarOpen = ref(true)
const isGenerating = ref(false)
const loadingMessage = ref('')

// Design configuration
const designConfig = reactive<DesignConfig>({
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

// Preview state
const currentViewport = ref<Viewport>('desktop')
const previewMode = ref<PreviewMode>('interactive')
const currentTheme = useLocalStorage<Theme>('ui-customizer-theme', 'system')

// Component state
const generatedComponents = ref<GeneratedComponent[]>([])
const availableComponents = ref<ComponentType[]>([
  'button', 'card', 'form', 'navigation', 'modal', 'table', 'layout'
])

// Event handlers
const handleThemeChange = (theme: Theme) => {
  currentTheme.value = theme
  applyTheme(theme)
}

const handleSaveProject = async () => {
  try {
    const projectData = {
      designConfig: designConfig,
      generatedComponents: generatedComponents.value,
      timestamp: new Date().toISOString()
    }
    
    localStorage.setItem('ui-customizer-project', JSON.stringify(projectData))
    
    notificationStore.addNotification({
      type: 'success',
      message: 'Project saved successfully',
      duration: 3000
    })
  } catch (error) {
    handleError(error, 'Failed to save project')
  }
}

const handleLoadProject = async () => {
  try {
    const savedProject = localStorage.getItem('ui-customizer-project')
    if (savedProject) {
      const projectData = JSON.parse(savedProject)
      
      Object.assign(designConfig, projectData.designConfig)
      generatedComponents.value = projectData.generatedComponents || []
      
      notificationStore.addNotification({
        type: 'success',
        message: 'Project loaded successfully',
        duration: 3000
      })
    }
  } catch (error) {
    handleError(error, 'Failed to load project')
  }
}

const generatePreview = async () => {
  if (isGenerating.value) return
  
  try {
    isGenerating.value = true
    loadingMessage.value = 'Generating component preview...'
    
    const response = await designStore.generateComponents(designConfig)
    generatedComponents.value = response.components
    
    notificationStore.addNotification({
      type: 'success',
      message: `Generated ${response.components.length} components`,
      duration: 2000
    })
  } catch (error) {
    handleError(error, 'Failed to generate preview')
  } finally {
    isGenerating.value = false
    loadingMessage.value = ''
  }
}

const handleComponentSelection = (componentType: ComponentType) => {
  console.log(`Component selected: ${componentType}`)
}

const handleComponentUpdate = (updatedComponent: GeneratedComponent) => {
  const index = generatedComponents.value.findIndex(c => c.id === updatedComponent.id)
  if (index !== -1) {
    generatedComponents.value[index] = updatedComponent
  }
}

const applyTheme = (theme: Theme) => {
  const html = document.documentElement
  
  if (theme === 'dark') {
    html.classList.add('dark')
  } else if (theme === 'light') {
    html.classList.remove('dark')
  } else {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    html.classList.toggle('dark', prefersDark)
  }
}

// Watch for design config changes
watch(
  () => designConfig,
  async (newConfig) => {
    clearTimeout(previewDebounceTimer)
    previewDebounceTimer = setTimeout(() => {
      generatePreview()
    }, 500)
  },
  { deep: true }
)

let previewDebounceTimer: NodeJS.Timeout

// Lifecycle hooks
onMounted(async () => {
  try {
    applyTheme(currentTheme.value)
    await generatePreview()
  } catch (error) {
    handleError(error, 'Failed to initialize application')
  }
})
</script>

<style scoped>
#app {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: rgb(156 163 175) transparent;
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgb(156 163 175);
  border-radius: 3px;
}
</style>