<template>
    <div class="index">
        <h1>This is an index page</h1>
        <router-link to="/create" class="btn btn-sm btn-primary"> Add Contact </router-link>
        <b-container class="bv-contact">
            <div v-if="contacts && contacts.length">
                <b-row class="card mb-3" v-for="contact of contacts" v-bind:key="contact.id">
                    <b-col>{{contact.name}}</b-col>
                    <b-col>{{contact.birthday}}</b-col>
                    <b-col>{{contact.message}}</b-col>
                </b-row>
            </div>
        </b-container>
        <p>No contacts</p>
    </div>
</template>



<script>

import axios from 'axios';

export default {
    data() {
        return {
            contacts: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        all: function () {
            axios.get('http://127.0.0.1:8000/api/contacts/')
                .then( response => {
                    this.contacts = response.data
                });
        }
    },
};
</script>
