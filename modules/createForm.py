from models.responseBodies import Form, StartSubmission

class CreateForm:
    def __init__(self) -> None:
        self.form = Form(
            id="XRAhBuOZ",
            type="quiz",
            title= "Buildform demo(copy)"
        )
        

    def get_form(self):
        return self.form

class StartFillingForm:
    def __init__(self) -> None:
        self.response = StartSubmission(
            signature="2090686e65677664313371756f76647239786777367a34686e656776643179616b6834313339363936363463366336363533373434333536343134353337366237613339343233303664373236613737353935613431363436393336343833313337333133383334333233313335333133343963376262313231613836623765383266393637616666303263626532363461396330333839656364303263383036613036663035303834656264633739326531373138343231353134",
            submission={
                "response_id": "hnegvd13quovdr9xgw6z4hnegvd1yakh",
                "type": "started",
                "form_id": "XRAhBuOZ",
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