<template>
    <div class="index">
        <h1>Contacts</h1>
        <router-link to="/create" class="btn btn-sm btn-primary"> Add Contact </router-link>
        <div v-if="contacts && contacts.length">
            <div v-for="contact of contacts" v-bind:key="contact.id">
                <div class="row no-gutters" style="padding:1em;">
                    <div class="col-md-4">
                        <svg class="bd-placeholder-img" width="200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>{{ contact.name }}</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">{{contact.birthday}}</text></svg>
                    </div>
                    <div class="col-md-4">
                        <div class="card-body">
                            <h5 class="card-title">{{ contact.name }}</h5>
                            <p class="card-text">{{ contact.phone_number }}</p>
                            <p class="card-text">{{ contact.message }}</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card-body">
                            <router-link :to="{name: 'Edit', params: { id: contact.id }}" class="btn btn-sm btn-primary">Edit</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteContact(contact)">Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>        
            <p>No contacts</p>
        </div>
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
        deleteContact: function(cont) {
            if (confirm('Delete ' + cont.name)) {
                axios.delete(`https://birthdayreminders-api.herokuapp.com/api/contacts/${cont.id}/`)
                    .then( response => {
                        console.log(response)
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('https://birthdayreminders-api.herokuapp.com/api/contacts/')
                .then( response => {
                    this.contacts = response.data
                });
        },
    },
};
</script>
