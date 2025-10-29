import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: () => import('../views/Dashboard.vue')
  },
  {
    path: '/trends',
    name: 'trends',
    component: () => import('../views/TrendMonitor.vue')
  },
  {
    path: '/projects',
    name: 'projects',
    component: () => import('../views/ProjectTracker.vue')
  },
  {
    path: '/ecosystem',
    name: 'ecosystem',
    component: () => import('../views/EcosystemMap.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
