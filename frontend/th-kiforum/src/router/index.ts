/**
 * router/index.ts
 *
 * Manual routes for ./src/pages/*.vue
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router'
import Index from '@/pages/index.vue'
import Impressum from '@/pages/impressum.vue'
import Datenschutz from '@/pages/datenschutz.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: Index,
    },
    {
      path: '/impressum',
      component: Impressum,
    },
    {
      path: '/datenschutz',
      component: Datenschutz,
    },
  ],
})

export default router
