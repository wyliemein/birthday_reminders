<template>
    <div class="pt-5">
        <ValidationObserver v-slot="{ invalid }">
            <form @submit.prevent="update" method="post">
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
                <div class="form-group">
                    <label for="birthday">Birthday</label>
                    <validation-provider rules="required" v-slot="{errors}">
                        <b-input-group class="mb-3">
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
                                placeholder="Time Message will be Sent"
                                locale="en"
                            ></b-form-timepicker>
                        </b-input-group>
                    <div class="invalid-feedback">
                        Please provide a valid date.
                    </div>
                    <span>{{ errors[0] }}</span>
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
            submitted: false
        }
    },
    mounted() {
        axios.get('https://birthdayreminders-api.herokuapp.com/api/contacts/' + this.$route.params.id+ '/')
            .then( response => {
                console.log(response.data)
                this.contact = response.data
            });
    },
    methods: {
        update: function (e) {
            console.log(e)
                axios.put(`https://birthdayreminders-api.herokuapp.com/api/contacts/${this.contact.id}/`,
                        this.contact
                    ).then(response => {
                        console.log(response.data)
                        this.$router.push('/contacts');
                    })
        },
    },
}
</script>