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
                "type": "started",
                "form_id": id,
            }
        )
        

    def get_form(self):
        return self.response
    
    def sign(self):
        # Create a unique numerical value that used as a signature
        return ''.join(random.choices('0123456789', k=128))
