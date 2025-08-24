// frontend/src/stores/notifications.ts
/**
 * Pinia store for notification management
 */

import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface Notification {
  id: string
  type: 'success' | 'error' | 'warning' | 'info'
  title: string
  message?: string
  duration?: number
  timestamp: string
}

export const useNotificationStore = defineStore('notifications', () => {
  // State
  const notifications = ref<Notification[]>([])

  // Actions
  const addNotification = (notification: Omit<Notification, 'id' | 'timestamp'>) => {
    const id = Date.now().toString()
    const newNotification: Notification = {
      ...notification,
      id,
      timestamp: new Date().toISOString(),
      duration: notification.duration || 5000
    }
    
    notifications.value.push(newNotification)
    
    // Auto-remove after duration
    if (newNotification.duration > 0) {
      setTimeout(() => {
        removeNotification(id)
      }, newNotification.duration)
    }
    
    return id
  }

  const removeNotification = (id: string) => {
    const index = notifications.value.findIndex(n => n.id === id)
    if (index > -1) {
      notifications.value.splice(index, 1)
    }
  }

  const clearAllNotifications = () => {
    notifications.value = []
  }

  return {
    notifications,
    addNotification,
    removeNotification,
    clearAllNotifications
  }
})