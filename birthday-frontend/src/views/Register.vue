<template>
  <div>
    <h4>Sign Up</h4>
    <form @submit.prevent="register">
      <label for="name">Name</label>
      <div>
          <input id="name" type="text" v-model="name" required autofocus>
      </div>

      <label for="username" >Username</label>
      <div>
          <input id="username" type="username" v-model="username" required>
      </div>

      <label for="password">Password</label>
      <div>
          <input id="password" type="password" v-model="password" required>
      </div>

      <label for="password-confirm">Confirm Password</label>
      <div>
        <b-col><input id="password-confirm" type="password" v-model="password_confirmation" required></b-col>
        <b-col><span v-if="password!==password_confirmation && password_confirmation !== ''"> Passwords do not match</span></b-col>
      </div>
      <span v-if="this.$store.getters.authStatus !== ''">Username already taken</span>
      <div style="padding: 1em;">
          <button type="submit" :disabled="password!==password_confirmation">Register</button>
      </div>
    </form>
    <router-link to='/login'>Back to Login</router-link>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        name : "",
        username : "",
        password : "",
        password_confirmation : "",
        is_admin : null
      }
    },
    methods: {
      register: function () {
        let data = {
          name: this.name,
          username: this.username,
          password: this.password,
          is_admin: this.is_admin
        }
        this.$store.dispatch('register', data)
       .then(() => this.$router.push('/contacts'))
       .catch(err => console.log(err))
      }
    }
  }
</script>

