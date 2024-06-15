from models.responseBodies import CompleteForm

class Submit:
    def __init__(self, form: CompleteForm) -> None:
        self.form = form

    def get_form(self):
        return self.form