import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store"

Vue.use(VueRouter);

const routes = [
  {
    path: "/contacts",
    name: "Index",
    component: () =>
      import(/* webpackChunkName: "index" */ "../views/Index.vue")
  },
  {
    path: "/create",
    name: "Create",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Create.vue")
  },
  {
    path: "/edit/:id",
    name: "Edit",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Edit.vue")
  },
  {
    path: "/login",
    name: "Login",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Login.vue")
  },
  {
    path: "/register",
    name: "Register",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Register.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if(!(to.name ==='Login' || to.name==='Register') && !store.getters.isLoggedIn){
    if(to.name == 'Register'){
      next({name: 'Register'})
    }
    next({name: 'Login'})
  } 
  else next()
})

export default router;
