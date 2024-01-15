import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import Management from "../views/Managementview.vue"
import Search from "../views/Searchview.vue"
import List from "../views/StudentList.vue"
import Editview from "../views/Editview.vue"
import ViewWrapper from "../components/ViewWrapper.vue"

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { 
      path: '/', 
      component: ViewWrapper,
      children: [
        { path: '/Home', component: Home },
        { path: '/Search', component: Search },
        { path: '/List', component: List },
        { path: '/Management', component: Management },
      ],
      redirect:'/Home'
    },  
    { path: '/Editstudent/:student', component: Editview, },
  ]
  
})

export default router
