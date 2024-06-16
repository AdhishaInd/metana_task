from fastapi import FastAPI

from modules.createForm import CreateForm, StartFillingForm
from modules.provider import StatProvider
from models.responseBodies import CompleteForm
from modules.submit import Submit

app = FastAPI()

forms: dict = {}


@app.get("/buildform-test")
async def buildform_test():
    new_form: CreateForm = CreateForm()
    forms[new_form.get_form().id] = {}
    return new_form.get_form()

@app.get("/forms/{formUid}/insights/submissions")
def get_submission_count(formUid: str):
    return StatProvider().get_submission_count()

# Get visiy_response_id from payload
@app.get("/forms/{formUid}/start-submission")
def start_submission(formUid: str):
    global forms
    # If formUid is not in forms, execption will be raised
    if formUid not in forms:
        raise Exception("Invalid formUid")

    forms[formUid] = StartFillingForm(formUid).get_form()
    return forms[formUid]

@app.post("/forms/{formUid}/complete-submission")
def complete_submission(formUid: str, form: CompleteForm):
    formsubmit = Submit(form, forms[formUid])
    if (formsubmit.verification()):
        # Insert form to the database
        formsubmit.submit()
        # Remove form from the forms
        del forms[formUid]
        return formsubmit.get_form()
    # execption will be raised if verification fails
    raise Exception("Invalid form")


@app.get("/forms/insights/events/v3/view-form-open")
def view_form_open(formUid: str):
    return {}

@app.get("/forms/{formUid}/insights/events/v3/see")
def see(formUid: str):
    return {}



