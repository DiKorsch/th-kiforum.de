// Utilities
import { defineStore } from 'pinia'

interface Organisation {
  id: string
  name: string
  description: string
  website: string
}

interface  User {
  id: string
  name: string
  email: string
  phone_number: string
}

interface Demo {
  id: string
  title: string
  description: string
  url: string
  key: string
  contact_person: User
  organisation: Organisation
}



export const useAppStore = defineStore('app', {
  state: () => ({
    demos: [] as Demo[]
  }),

  getters: {
    getDemos: (state) => state.demos,

    filterDemos: (state) => (searchTerm: string) => {
      return state.demos.filter((demo) =>
        demo.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        demo.description.toLocaleLowerCase().includes(searchTerm.toLowerCase()) ||
        demo.organisation.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        demo.contact_person.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        demo.key.toLowerCase().includes(searchTerm.toLowerCase())
      )
    },
  },

  actions: {
    setDemos(demos: Demo[]) {
      this.demos = demos
    }
  }

})
