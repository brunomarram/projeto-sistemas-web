import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Receitas from '../views/Receitas.vue'
import Receita from '../views/Receita.vue'

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/cadastrar",
    name: "Register",
    component: Register
  },
  {
    path: "/receitas",
    name: "Receitas",
    component: Receitas
  },
  {
    path: "/receita/:id",
    name: "Receita",
    component: Receita
  }
]

const router = new VueRouter({ routes, mode: "history" })

export default router
