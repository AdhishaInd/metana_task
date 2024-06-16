from models.responseBodies import CompleteForm, StartSubmission
from database.database import CRUD

import re

import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

class Submit:
    def __init__(self, form: CompleteForm, createForm: StartSubmission) -> None:
        self.form = form
        self.startForm = createForm

    def get_form(self):
        return self.form
    
    def verification(self):
        # Check if the form is filled correctly

        # Not empty not have any numbers or special characters
        if not self.form.firstname.isalpha():
            print("firstname")
            return False   
        if not self.form.lastname.isalpha():
            print("lastname")
            return False
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', self.form.email):
            print("email")
            return False
        if not self.countryValidator():
            print("country")
            return False
        # if not carrier._is_mobile(number_type(phonenumbers.parse(self.form.phonenumber))):
        #     print("phonenumber")
            return False
        if self.form.languages == []:
            print("languages")
            return False
        if self.experienceValidator():
            print("experience")
            return False
        # if self.compensationValidator():
        #     print("compensation")
            return False
        if self.form.acknowledgement == False:
            print("acknowledgement")
            return False
        if not re.fullmatch(r'https://www.linkedin.com/in/[A-Za-z0-9-]+', self.form.linkedin):
            print("linkedin")
            return False
        if self.form.landed_at == 0:
            print("landed_at")
            return False
        if self.form.signature != self.startForm.signature:
            print("signature")
            return False
        
        return True
    
    def countryValidator(self):
        countries = [ "United States", "United Kingdom", "China", "Canada", "United Arab Emirates", "Australia", "Andorra", "Afghanistan", "Antigua and Barbuda", "Anguilla", "Albania", "Armenia", "Angola", "Antarctica", "Argentina", "American Samoa", "Austria", "Aruba", "Azerbaijan", "Bosnia and Herzegovina", "Barbados", "Bangladesh", "Belgium", "Burkina Faso", "Bulgaria", "Bahrain", "Burundi", "Benin", "Saint Barthelemy", "Bermuda", "Brunei", "Bolivia", "Brazil", "Bahamas, The", "Bhutan", "Bouvet Island", "Botswana", "Belarus", "Belize", "Cocos (Keeling) Islands", "Congo, Democratic Republic of the", "Central African Republic", "Congo, Republic of the", "Switzerland", "Cote d'Ivoire", "Cook Islands", "Chile", "Cameroon", "Colombia", "Costa Rica", "Cuba", "Cape Verde", "Curacao", "Christmas Island", "Cyprus", "Czech Republic", "Germany", "Djibouti", "Denmark", "Dominica", "Dominican Republic", "Algeria", "Ecuador", "Estonia", "Egypt", "Western Sahara", "Eritrea", "Spain", "Ethiopia", "Finland", "Fiji", "Falkland Islands (Islas Malvinas)", "Micronesia, Federated States of", "Faroe Islands", "France", "France, Metropolitan", "Gabon", "Grenada", "Georgia", "French Guiana", "Guernsey", "Ghana", "Gibraltar", "Greenland", "Gambia, The", "Guinea", "Guadeloupe", "Equatorial Guinea", "Greece", "South Georgia and the Islands", "Guatemala", "Guam", "Guinea-Bissau", "Guyana", "Hong Kong (SAR China)", "Heard Island and McDonald Islands", "Honduras", "Croatia", "Haiti", "Hungary", "Indonesia", "Ireland", "Israel", "Isle of Man", "India", "British Indian Ocean Territory", "Iraq", "Iran", "Iceland", "Italy", "Jersey", "Jamaica", "Jordan", "Japan", "Kenya", "Kyrgyzstan", "Cambodia", "Kiribati", "Comoros", "Saint Kitts and Nevis", "Korea, South", "Kuwait", "Cayman Islands", "Kazakhstan", "Laos", "Lebanon", "Saint Lucia", "Liechtenstein", "Sri Lanka", "Liberia", "Lesotho", "Lithuania", "Luxembourg", "Latvia", "Libya", "Morocco", "Monaco", "Moldova", "Montenegro", "Saint Martin", "Madagascar", "Marshall Islands", "Macedonia", "Mali", "Burma", "Mongolia", "Macau (SAR China)", "Northern Mariana Islands", "Martinique", "Mauritania", "Montserrat", "Malta", "Mauritius", "Maldives", "Malawi", "Mexico", "Malaysia", "Mozambique", "Namibia", "New Caledonia", "Niger", "Norfolk Island", "Nigeria", "Nicaragua", "Netherlands", "Norway", "Nepal", "Nauru", "Niue", "New Zealand", "Oman", "Panama", "Peru", "French Polynesia", "Papua New Guinea", "Philippines", "Pakistan", "Poland", "Saint Pierre and Miquelon", "Pitcairn Islands", "Puerto Rico", "Gaza Strip", "West Bank", "Portugal", "Palau", "Paraguay", "Qatar", "Reunion", "Romania", "Serbia", "Russia", "Rwanda", "Saudi Arabia", "Solomon Islands", "Seychelles", "Sudan", "Sweden", "Singapore", "Saint Helena, Ascension, and Tristan da Cunha", "Slovenia", "Svalbard", "Slovakia", "Sierra Leone", "San Marino", "Senegal", "Somalia", "Suriname", "South Sudan", "Sao Tome and Principe", "El Salvador", "Sint Maarten", "Syria", "Swaziland", "Turks and Caicos Islands", "Chad", "French Southern and Antarctic Lands", "Togo", "Thailand", "Tajikistan", "Tokelau", "Timor-Leste", "Turkmenistan", "Tunisia", "Tonga", "Turkey", "Trinidad and Tobago", "Tuvalu", "Taiwan, Province of China", "Tanzania", "Ukraine", "Uganda", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Holy See (Vatican City)", "Saint Vincent and the Grenadines", "Venezuela", "British Virgin Islands", "Virgin Islands", "Vietnam", "Vanuatu", "Wallis and Futuna", "Samoa", "Kosovo", "Yemen", "Mayotte", "South Africa", "Zambia", "Zimbabwe" ]
        if self.form.country not in countries:
            return False
        return True
    
    def experienceValidator(self):
        experiences = ["No experience (I have never programmed before.)", "Beginner (I have played with some introductory coding lessons and tutorials.)", "Intermediate (I have completed some coding classes or tutorials", "Advanced (I can build applications.)", "Professional (I am an experienced software engineer.)"]
        if self.form.experience not in experiences:
            return False
        return True
    
    def compensationValidator(self):
        ranges = [ "<$30,000", "$30,000 - $50,000", "$50,000 - $80,000", "$80,000 - $120,000", "$120,000 - $250,000", "$250,000 or more" ]
        if self.form.compensation not in ranges:
            return False
        return True
    
    def submit(self):
        # Insert the form to the database
        return CRUD().insert_submission(self.form)