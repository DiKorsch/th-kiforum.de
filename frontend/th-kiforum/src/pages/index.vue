<template>
  <v-container class="fill-height d-flex flex-column justify-center" max-width="1100">
    <v-row>
      <v-col cols="12" md="6">
        <div class="text-h4 font-weight-bold mb-2">
          Demonstratoren
        </div>
        <div class="text-body-large font-weight-light mb-4">
          Hier finden Sie eine Übersicht über die Demonstratoren, die im Rahmen des KI-Forums vorgestellt werden.
        </div>
      </v-col>
      <v-col cols="12" md="6">
        <v-text-field
          v-model="filter"
          label="Suche"
          variant="outlined"
          clearable
          class="mb-4"
        />
        <v-checkbox
          v-model="onlySelected"
          :label="`Nur ausgewählte Demonstratoren anzeigen (${nSelectedDemos}/${appStore.demos.length})`"
        >
        </v-checkbox>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        v-for="demo in demos"
        :key="demo.id"
        cols="12" md="6"
      >
        <v-card
          class="py-4 mb-4"
          color="surface-variant"
          rounded="lg"
          variant="tonal"
          min-height="200"
        >
          <v-card-title>
            <div class="text-h6 font-weight-bold d-flex align-center">
              {{ demo.title }}
            <v-icon
              :color="selectedDemos.includes(demo.key) ? 'success' : 'grey'"
              class="ml-auto"
              @click="toggle(demo)"
            >
              {{ icon(demo) }}
            </v-icon>
            </div>
          </v-card-title>

          <v-card-text>
            <div class="text-body-large">
              {{ demo.description }}
            </div>
          </v-card-text>
          <v-card-actions>
            <v-row>
              <v-col cols="12" md="4">
                <div class="text-body-large font-weight-light mb-n1">
                  <v-btn :href="`mailto:${demo.contact_person.email}`" variant="text" prepend-icon="mdi-account">
                    {{ demo.contact_person.name }}
                  </v-btn>
                </div>
              </v-col>
              <v-col cols="12" md="4">
                <div class="text-body-medium font-weight-light mb-n1">
                  <v-btn :href="demo.organisation.website" target="_blank" rel="noopener noreferrer" variant="text" prepend-icon="mdi-domain">
                  {{ demo.organisation.name }}
                  </v-btn>
                </div>
              </v-col>

              <v-col cols="12" md="4">
                <div class="text-body-medium font-weight-light mb-n1">
                  <v-btn :href="demo.url" target="_blank" rel="noopener noreferrer" prepend-icon="mdi-information">
                    Weitere Infos
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>

      </v-col>
  </v-row>

  </v-container>

</template>

<script lang="ts" setup>
  import { useAppStore } from '@/stores/app'
  const appStore = useAppStore()

  import { computed, ref, onMounted } from 'vue'

  const filter = ref('')
  const selectedDemos = ref([] as string[])
  const onlySelected = ref(false)

  const nSelectedDemos = computed(() => {
    return appStore.demos.filter((demo) => selectedDemos.value.includes(demo.key)).length
  })

  const demos = computed(function getDemos() {

    let demos = []
    if (!filter.value || filter.value.trim() === '') {
      demos =  appStore.demos
    }
    demos =  appStore.filterDemos(filter.value)
    if (onlySelected.value) {
      return demos.filter((demo) => selectedDemos.value.includes(demo.key))
    }
    return demos
  })

  const icon = computed(() => (demo: any) => {
    if (selectedDemos.value.includes(demo.key)) {
      return 'mdi-check-circle'
    } else {
      return 'mdi-circle'
    }
  })

  const toggle = (demo: any) => {
    if (selectedDemos.value.includes(demo.key)) {
      selectedDemos.value = selectedDemos.value.filter((key: string) => key !== demo.key)
    } else {
      selectedDemos.value.push(demo.key)
    }
    localStorage.setItem('selectedDemos', JSON.stringify(selectedDemos.value))
  }

  onMounted(() => {
    selectedDemos.value = JSON.parse(localStorage.getItem('selectedDemos') || '[]')
  })

</script>
