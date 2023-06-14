import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../views/Layout.vue'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileFormView from '../views/ProfileFormView.vue'
import ContactsView from '../views/ContactsView.vue'
import MedicalView from '../views/MedicalView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/app',
    name: 'Layout',
    component: Layout,
    children: [
      {
        path: 'home',
        component: HomeView,
      },
      {
        path: 'profileform',
        component: ProfileFormView
      },
      {
        path: 'contacts',
        component: ContactsView
      },
      {
        path: 'medical',
        component: MedicalView
      }
    ],
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router