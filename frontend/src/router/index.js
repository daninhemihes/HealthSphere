import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../views/Layout.vue'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

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
        path: 'profile',
        component: HomeView,
      },
    ],
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router