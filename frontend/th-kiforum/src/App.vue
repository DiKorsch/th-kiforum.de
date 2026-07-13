<template>
  <v-layout ref="app" class="rounded rounded-md ">
    <AppBar/>

    <v-main class="d-flex align-center justify-center">
      <router-view/>
    </v-main>

    <FooterPanel/>

  </v-layout>
</template>

<script lang="ts" setup>
  import AppBar from '@/components/AppBar.vue'
  import FooterPanel from '@/components/FooterPanel.vue'
  import { useAppStore } from '@/stores/app'
  import { ref, onMounted, computed } from 'vue'

  const appStore = useAppStore()
  const BASE_BACKEND_URL = import.meta.env.VITE_BACKEND_URL + '/api/v1'

  onMounted(() => {
    fetch(`${BASE_BACKEND_URL}/demonstrators/`)
      .then(response => response.json())
      .then(data => {
        appStore.setDemos(data)
      })
      .catch(error => {
        console.error('Error fetching demos:', error)
      })
  })
</script>
