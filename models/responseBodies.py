from pydantic import BaseModel

class Form(BaseModel):
    id: str
    type: str
    title: str

# ------------------------- StartSubmission -------------------------

class Submission(BaseModel):
    type: str
    form_id: str

class StartSubmission(BaseModel):
    signature: str
    submission: Submission

#-----------------------------------------------------------------

class CompleteForm(BaseModel):
    firstname: str
    lastname: str
    email: str
    country: str
    phonenumber: str
    languages: list[str]
    experience: str
    compensation: str
    acknowledgement: bool
    linkedin: str
    signature: str