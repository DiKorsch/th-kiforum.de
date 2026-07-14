<template>
  <v-container class="fill-height d-flex flex-column justify-center" max-width="1100">
    <h1>{{props.title}}</h1>
    <div ref="content"></div>
  </v-container>

</template>

<script setup>
import { useTemplateRef, onMounted, ref } from 'vue';

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  contentName: {
    type: String,
    required: true
  }
});

const content = useTemplateRef('content');

const BASE_BACKEND_URL = import.meta.env.VITE_BACKEND_URL

onMounted(() => {
  fetch(BASE_BACKEND_URL + `/content/${props.contentName}`)
    .then(response => response.json())
    .then(data => {
      if (content.value) {
        content.value.innerHTML = data.html;
      }
    })
    .catch(error => {
      console.error('Error fetching impressum content:', error);
    });
})

</script>
