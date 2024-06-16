from database.database import CRUD

class StatProvider:
    def __init__(self) -> None:
        self.submissions = CRUD().get_submissions_count()

    def get_submission_count(self):
        return {"submissions": self.submissions}