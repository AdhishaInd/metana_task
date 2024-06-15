from pydantic import BaseModel

class Form(BaseModel):
    id: str
    type: str
    title: str

# ------------------------- StartSubmission -------------------------
class MetaData(BaseModel):
    user_agent: str
    platform: str
    referer: str
    network_id: str
    ip: str
    browser: str
    client: str
    id_type: str
    source: str
    medium: str
    medium_version: str
    embed_trigger_type: str
    domain_type: str
    subdomain_type: str

class Submission(BaseModel):
    response_id: str
    type: str
    form_id: str
    landed_at: int
    visit_response_id: str
    metadata: MetaData

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
    compensation: int
    acknowledgement: bool
    linkedin: str
    landed_at: int
    signature: str