// frontend/src/composables/useErrorHandler.ts
/**
 * Composable for centralized error handling
 */

import { ref } from 'vue'
import { useNotificationStore } from '../stores/notifications'

export interface ErrorDetails {
  message: string
  code?: string
  details?: any
}

export function useErrorHandler() {
  const notificationStore = useNotificationStore()
  const currentError = ref<ErrorDetails | null>(null)

  const handleError = (error: any, context?: string) => {
    console.error('Error occurred:', error, 'Context:', context)
    
    let errorMessage = 'An unexpected error occurred'
    let errorCode = 'UNKNOWN_ERROR'
    
    if (error instanceof Error) {
      errorMessage = error.message
    } else if (typeof error === 'string') {
      errorMessage = error
    } else if (error?.message) {
      errorMessage = error.message
      errorCode = error.code || errorCode
    }
    
    const errorDetails: ErrorDetails = {
      message: context ? `${context}: ${errorMessage}` : errorMessage,
      code: errorCode,
      details: error
    }
    
    currentError.value = errorDetails
    
    // Show notification
    notificationStore.addNotification({
      type: 'error',
      title: 'Error',
      message: errorDetails.message,
      duration: 5000
    })
  }

  const clearError = () => {
    currentError.value = null
  }

  return {
    currentError,
    handleError,
    clearError
  }
}