from typing import Optional

from fastapi import FastAPI

from modules.createForm import CreateForm, StartFillingForm
from modules.provider import StatProvider
from models.responseBodies import CompleteForm
from modules.submit import Submit

app = FastAPI()


@app.get("/buildform-test")
async def buildform_test():
    return CreateForm().get_form()

@app.get("/forms/{formUid}/insights/submissions")
def get_submission_count(formUid: str):
    return StatProvider().get_submission_count()

@app.get("/forms/insights/events/v3/view-form-open")
def view_form_open(formUid: str):
    return {}

@app.get("/forms/{formUid}/insights/events/v3/see")
def see(formUid: str):
    return {}

# Get visiy_response_id from payload
@app.get("/forms/{formUid}/start-submission")
def start_submission(formUid: str):
    return StartFillingForm().get_form()

@app.post("/forms/{formUid}/complete-submission")
def complete_submission(formUid: str, form: CompleteForm):
    formsubmit = Submit(form)
    return formsubmit.get_form()