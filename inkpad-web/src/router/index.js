import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Theory from '../views/Theory.vue'
import Apps from '../views/Apps.vue'
import AppDownload from '../views/AppDownload.vue'
import Login from '../views/Login.vue'
import MoreDetail from '../views/MoreDetail.vue'

const routes = [
  { path: '/', name: 'Inkpad', component: Home },
  { path: '/home', name: 'Home', component: Home },
  { path: '/theory', name: 'Theory', component: Theory },
  { path: '/apps', name: 'Apps', component: Apps },
  { path: '/app-download', name: 'AppDownload', component: AppDownload },
  { path: '/login', name: 'Login', component: Login },
  { path: '/more/:id', name: 'MoreDetail', component: MoreDetail },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
