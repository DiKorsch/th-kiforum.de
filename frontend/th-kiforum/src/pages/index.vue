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
              {{ dotify(demo.title, 30) }}
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
              {{ dotify(demo.description, 300) }}
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
                  <v-btn @click="moreInfo = demo.key" target="_blank" rel="noopener noreferrer" prepend-icon="mdi-information">
                    Weitere Infos
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>

      </v-col>
  </v-row>

    <v-dialog
      v-model="moreInfoIsOpen"
      width="auto"
    >
      <v-card class="mx-auto" max-width="1600">
        <v-card-title class="d-flex justify-space-between align-center">
          <div class="text-headline-small text-medium-emphasis ps-2">
            {{moreInfoTitle}}
          </div>
          <v-btn
            icon="mdi-close"
            variant="text"
            @click="moreInfo = undefined"
          ></v-btn>
        </v-card-title>
        <v-card-subtitle class="d-flex justify-space-between align-center">
          <div class="text-body-medium text-medium-emphasis ps-2">
            Demonstrator von {{ moreInfoOrganisationName }}
          </div>
        </v-card-subtitle>
        <v-card-text class="d-flex justify-space-between align-center">
          <div class="text-medium-emphasis mb-4 ps-2">
            {{moreInfoText}}
          </div>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions class="d-flex justify-space-between align-center">

          <v-row class="ps-2">
            <v-col cols="12" md="4">
              <div class="text-body-large font-weight-light mb-n1">
                <v-btn :href="`mailto:${moreInfoEmail}`" variant="text" prepend-icon="mdi-account">
                  {{ moreInfoName }}
                </v-btn>
              </div>
            </v-col>
            <v-col cols="12" md="4">
              <div class="text-body-medium font-weight-light mb-n1">
                <v-btn :href="moreInfoWebsite" target="_blank" rel="noopener noreferrer" variant="text" prepend-icon="mdi-domain">
                {{ moreInfoOrganisationName }}
                </v-btn>
              </div>
            </v-col>
            <v-col cols="12" md="4">
              <v-btn
                v-if="moreInfoDemo !== undefined"
                :append-icon="icon(moreInfoDemo)"
                :color="selectedDemos.includes(moreInfoDemo.key) ? 'success' : 'grey'"
                @click="toggle(moreInfoDemo)"
              >
                {{ selectedDemos.includes(moreInfoDemo.key) ? 'Ausgewählt' : 'Auswählen' }}
              </v-btn>
              <v-icon

                class="ml-auto"
              >
                {{  }}
              </v-icon>
            </v-col>

          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>

</template>

<script lang="ts" setup>
  import { useAppStore } from '@/stores/app'
  const appStore = useAppStore()

  import { computed, ref, onMounted } from 'vue'

  const filter = ref('')
  const selectedDemos = ref([] as string[])
  const onlySelected = ref(false)
  const moreInfo = ref(undefined as any)

  const nSelectedDemos = computed(() => {
    return appStore.demos.filter((demo) => selectedDemos.value.includes(demo.key)).length
  })

  const moreInfoIsOpen = computed({
    get: () => {
      return moreInfo.value !== undefined
    },
    set: (value: boolean) => {
      if (!value) {
        moreInfo.value = undefined
      }
    }
  })

  const moreInfoDemo = computed(() => {
    if (moreInfo.value === undefined) {
      return undefined
    }
    return appStore.demos.find((demo) => demo.key === moreInfo.value)
  })

  const moreInfoTitle = computed(() => {
    return moreInfoDemo.value?.title || ''
  })

  const moreInfoText = computed(() => {
    return moreInfoDemo.value?.description || ''
  })

  const moreInfoEmail = computed(() => {
    return moreInfoDemo.value?.contact_person.email || ''
  })

  const moreInfoName = computed(() => {
    return moreInfoDemo.value?.contact_person.name || ''
  })

  const moreInfoWebsite = computed(() => {
    return moreInfoDemo.value?.organisation.website || ''
  })

  const moreInfoOrganisationName = computed(() => {
    return moreInfoDemo.value?.organisation.name || ''
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
    if (selectedDemos.value.includes(demo?.key)) {
      return 'mdi-check-circle'
    } else {
      return 'mdi-circle'
    }
  })

  const dotify = computed(() => (title: string, n_chars: number) => {
    // if title is longer than n_chars characters, truncate it and add "..." at the end
    if (title.length > n_chars) {
      return title.substring(0, n_chars) + '...'
    }
    return title
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
