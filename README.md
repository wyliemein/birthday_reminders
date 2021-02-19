# birthday_reminders
Simple CRUD app for your contacts that allows you to send scheduled, customized messages to your friends on their birthday.

Uses:
Vue.js,
Django,
Twilio SMS API,
Dramatiq,
Redis,
Heroku,

Site is Live at: 
https://birthdayreminders.herokuapp.com

Current Issues:
- Free heroku redis account doesn't support many connections
- Twilio is expensive
- Date time offset is subject to failure with time change 
- Very basic auth, not very secure

Goals for future:
- Add throttling to auth or captcha 
- add Oauth2 (or other auth options) with password resets
- Update UI for better error messaging
- More space to store tasks, so after message is sent be able to store again for next year

How To Use Locally:
1. clone the repository
2. pip install --requirments
3. install redis and dramatiq
4. update Twilio Account in settings.py to personal account 
5. start Vue.js fronted (need to update axios requests to local server)
6. start Django backend
7. start redis
8. start dramatiq
9. use on local server

To activate virtual environment: source ./env/bin/activate
run django: python manage.py runserver
run frontend: npm run

Note: running locally depends on a .env file that contains enviroment variables for local dev, an example file to see what format is needed is provided with /env-example but will not work as is. 
