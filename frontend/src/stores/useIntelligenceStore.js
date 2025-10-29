import { defineStore } from 'pinia'
import client from '../api/client'

export const useIntelligenceStore = defineStore('intelligence', {
  state: () => ({
    loading: false,
    items: [],
    report: null,
    graph: null,
    lastUpdated: null,
    error: null
  }),
  actions: {
    async refreshData(sources = []) {
      this.loading = true
      this.error = null
      try {
        const response = await client.post('/api/data/refresh', { sources })
        this.items = response.data.items
        this.lastUpdated = response.data.updated_at
      } catch (error) {
        this.error = error.response?.data?.detail || error.message
      } finally {
        this.loading = false
      }
    },
    async loadData() {
      this.loading = true
      this.error = null
      try {
        const response = await client.get('/api/data')
        this.items = response.data.items
        this.lastUpdated = response.data.updated_at
      } catch (error) {
        this.error = error.response?.data?.detail || error.message
      } finally {
        this.loading = false
      }
    },
    async loadReport() {
      this.error = null
      try {
        const response = await client.get('/api/report')
        this.report = response.data
      } catch (error) {
        this.error = error.response?.data?.detail || error.message
      }
    },
    async loadGraph() {
      this.error = null
      try {
        const response = await client.get('/api/graph')
        this.graph = response.data
      } catch (error) {
        this.error = error.response?.data?.detail || error.message
      }
    }
  }
})
