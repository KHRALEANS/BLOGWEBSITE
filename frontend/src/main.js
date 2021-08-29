import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import "bootstrap"
import "bootstrap-icons/font/bootstrap-icons.css"
import routers from "@/routers";

const app = createApp(App)
app.use(routers)
app.mount('#app')
app.config.globalProperties.$http = axios
