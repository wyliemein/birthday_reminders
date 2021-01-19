<template>
    <div class="index">
        <h1>This is an index page</h1>
        <div v-if="subscriptions && subscriptions.length">
            
        </div>
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
