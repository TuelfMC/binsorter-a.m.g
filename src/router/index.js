import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import EscanerView from '../views/EscanerView.vue'

const routes = [
  { path: '/home', component: HomeView },
  { path: '/login', component: LoginView },
  { path: '/register', component: RegisterView },
    { path: '/escaner', component: EscanerView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})