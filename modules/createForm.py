from models.responseBodies import Form, StartSubmission

import random

class CreateForm:
    def __init__(self) -> None:
        self.form = Form(
            id=self.createId(),
            type="quiz",
            title= "Buildform demo(copy)"
        )
        

    def get_form(self):
        return self.form
    
    def createId(self):
        # Create a unique id only lower case and upper case letters randomly generated
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))


class StartFillingForm:
    def __init__(self, id: str) -> None:
        self.response = StartSubmission(
            signature=self.sign(),
            submission={
                "response_id": "hnegvd13quovdr9xgw6z4hnegvd1yakh",
                "type": "started",
                "form_id": id,
                "landed_at": 1718421514,
                "visit_response_id": "ncE467A4nMS4",
                "metadata": {
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
                    "platform": "other",
                    "referer": "https://metana.typeform.com/buildform-test",
                    "network_id": "29c42580fb",
                    "ip": "206.189.145.210",
                    "browser": "default",
                    "client": "stakhanov",
                    "id_type": "form-alias",
                    "source": "",
                    "medium": "",
                    "medium_version": "",
                    "embed_trigger_type": "",
                    "domain_type": "standard",
                    "subdomain_type": "custom"
                } 
            }
        )
        

    def get_form(self):
        return self.response
    
    def sign(self):
        # Create a unique numerical value that used as a signature
        return ''.join(random.choices('0123456789', k=128))
