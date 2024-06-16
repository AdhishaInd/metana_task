# API Documentation
This api has 4 main endpoints
1. **{baseurl}/buildform-test** Get a unique formUid id that required for other requests
2. **{baseurl}/form/{formUid}/submissions** Get the total number of submissions the form have
3. **{baseurl}/form/{formUid}/start-submission** Start the filling prcess and respond with a signature that used to prove a submission
4. **{baseurl}/form/{formUid}/complete-submission** Send the completed form to the server where it writen to a database

For the database, I used **SQLite**

# 1 Build form-test
Get request and respond with **{"id":{formUid},"type":"quiz","title":"Buildform demo(copy)"}**
# 2 Submissions
Get request and respond with **{"submissions":{submission count}}**
# 3 Start submission
Get request and it will initilize the process buy creating a signature and responding **{"signature": {signature}}**
# 4 complete submission
POST request and it will write the respond to the database. Refer this example for the request body
**{ "firstname": "John", "lastname": "Doe", "email": "johndoe@example.com", "country": "United States", "phonenumber": "+1234567890", "languages": ["Python", "Java"], "experience": "No experience (I have never programmed before.)", "compensation": "<$30,000", "acknowledgement": true, "linkedin": "https://www.linkedin.com/in/johndoe", "landed_at": 1655187200, "signature": "95187892956355300592766503834241181147499506675834140434117204673513231725035207679855012659581241508517494767750334309981343744" }'**