<template>
    <div class="pt-5">
        <ValidationObserver v-slot="{ invalid }">
            <form @submit.prevent="create" method="post">
                <div class="form-group">
                    <label for="name">Name</label>
                    <validation-provider rules="required" v-slot="{errors}">
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
                    <span>{{ errors[0] }}</span>
                    </validation-provider>
                </div>
                <div class="form-group inline">
                    <label for="birthday">Birthday</label>
                    <validation-provider rules="required">
                        <b-input-group>
                            <b-input-group-prepend>
                                <b-form-datepicker
                                v-model="contact.birthday"
                                button-only
                                right
                                locale="en-US"
                                aria-controls="example-input"
                                ></b-form-datepicker>
                            </b-input-group-prepend>
                            <b-form-input
                                id="example-input"
                                v-model="contact.birthday"
                                type="text"
                                placeholder="YYYY-MM-DD"
                                autocomplete="off"
                                class="w-25"
                                :class="{'is-invalid': 'errors.name' && submitted}"
                            ></b-form-input>
                            <b-form-timepicker
                                v-model="contact.time"
                                placeholder="Time"
                                locale="en"
                            ></b-form-timepicker>
                        </b-input-group>
                    </validation-provider>
                </div>
                <div class="form-group">
                    <label for="phone_number">Phone Number</label>
                    <validation-provider rules="required" v-slot="{errors}">
                    <vue-phone-number-input v-model="contact.phone_number">
                    </vue-phone-number-input>
                    <span>{{ errors[0] }}</span>
                    </validation-provider>
                </div>
                <div class="form-group">
                    <label for="message">message</label>
                    <validation-provider rules="required" v-slot="{errors}">
                    <textarea
                        name="message"
                        class="form-control"
                        id="message"
                        v-model="contact.message"
                        cols="30"
                        rows="2"
                        placeholder="Happy Birthday!"
                        :class="{'is-invalid': 'errors.message' && submitted}"></textarea>
                    <div class="invalid-feedback">
                        Please provide a valid message.
                    </div>
                    <span>{{ errors[0] }}</span>
                    </validation-provider>
                </div>
                <button type="submit" :disabled="invalid" class="btn btn-primary">Submit</button>
            </form>
        </ValidationObserver>
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
                time: '',
                owner_id: '',
            },
            errors: '',
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            console.log(e)
            this.contact.owner_id = this.$store.getters.currUser;
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