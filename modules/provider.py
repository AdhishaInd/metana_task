class StatProvider:
    def __init__(self) -> None:
        self.submissions = 62

    def get_submission_count(self):
        return {"submissions": self.submissions}