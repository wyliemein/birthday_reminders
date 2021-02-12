<template>
 <div>
    <h1>Birthday Reminders</h1>
   <form class="Login" @submit.prevent="login">
     <b-col>
      <h3>Sign in</h3>
     </b-col>
     <b-col>
      <label>Username</label>
     </b-col>
     <b-col>
      <input required v-model="username" type="username" placeholder="Name"/> 
     </b-col>
      <b-col>
      <label>Password</label>
     </b-col>
     <b-col>
      <input required v-model="password" type="password" placeholder="Password"/>
     </b-col>
        <span v-if="this.$store.getters.authStatus === 'error'">Username or Password Incorrect</span>
     <hr>
      <b-col><button type="submit">Login</button></b-col>
      <b-col><router-link to="/register">Or Sign Up!</router-link></b-col>
   </form>
 </div>
</template>

<script>
export default {
  data(){
    return {
      username : "",
      password : "",
    }
  },
  methods: {
    login: function () {
      let username = this.username
      let password = this.password
      this.$store.dispatch('login', { username, password })
      .then(() => this.$router.push('/contacts'))
      .catch(err => console.log(err))
    }
  },
}
</script>