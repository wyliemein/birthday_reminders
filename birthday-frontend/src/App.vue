<template>
  <div id="app">
    <div id="nav" style="display: flex; justify-content: flex-end">
      <div class="routing" v-if="this.$route.path !== '/login'">
        <span v-if="isLoggedIn"> <router-link v-if="this.$route.path !== '/contacts'" to="/contacts">Contacts | </router-link><a @click="logout">Logout</a></span>
      </div>
    </div>
    <router-view /> 
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
  export default {
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
    },
    created: function () {
      this.$http.interceptors.response.use(undefined, function (err) {
        return new Promise(function () {
          if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
            this.$store.dispatch('logout')
          }
          throw err;
        });
      });
    },
    methods: {
      logout: function () {
        if(confirm("Do you want to Logout?")){
          this.$store.dispatch('logout')
          .then(() => {
            this.$router.push('/login')
          })
        }
      }
    },
  }
</script>