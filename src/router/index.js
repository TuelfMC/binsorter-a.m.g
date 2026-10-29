import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/login', component: LoginView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})