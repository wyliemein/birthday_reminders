<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="name">Name</label>
                <ValidationProvider rules="required">
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="contact.name"
                    name="name"
                    placeholder="Enter name"
                    :class="{'is-invalid': 'errors.name' && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
                </ValidationProvider>
            </div>
            <div class="form-group">
                <label for="birthday">Birthday</label>
                <ValidationProvider rules="required">
                <b-form-datepicker 
                    id="borthday-datepicker" 
                    v-model="contact.birthday" 
                    class="mb-2">
                </b-form-datepicker>
                <p>Birthday: '{{contact.birthday}}'</p>
                <div class="invalid-feedback">
                    Please provide a valid date.
                </div>
                </ValidationProvider>
            </div>
            <div class="form-group">
                <label for="phone_number">Phone Number</label>
                <ValidationProvider rules="required">
                <input
                    type="number"
                    name="phone_number"
                    class="form-control"
                    id="phone_number"
                    v-model="contact.phone_number"
                    placeholder="Enter phone_number"
                    :class="{'is-invalid': 'errors.phone_number' && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid Phone Number.
                </div>
                </ValidationProvider>
            </div>
            <div class="form-group">
                <label for="message">message</label>
                <ValidationProvider rules="required">
                <textarea
                    name="message"
                    class="form-control"
                    id="message"
                    v-model="contact.message"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': 'errors.message' && submitted}"></textarea>
                <div class="invalid-feedback">
                    Please provide a valid message.
                </div>
                </ValidationProvider>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>



<script>

import axios from 'axios';

export default {
    data() {
        return {
            contact: {
                name: '',
                message: '',
                phone_number: '',
                birthday: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            console.log(e)
            this.submitted = true;
                axios.post('http://127.0.0.1:8000/api/contacts/',
                        this.contact
                    )
                    .then(response => {
                        console.log(response)
                        this.$router.push('/contacts');
                    })
        },
    },
}

</script>