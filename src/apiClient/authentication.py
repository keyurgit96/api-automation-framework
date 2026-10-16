import json
import os
from src.apiClient.api_client import baseAPI
from src.config.endpoints import Endpoints


class loginAPI(baseAPI):
    def __init__(self, baseURL=None, session=None):
        super().__init__(baseURL, session)

    def login(self, payload: dict):
        self.response = self.post(Endpoints.AUTH_LOGIN, payload)
        return self.response

    def getProfile(self, token: str = None, headers: dict = None, **kwargs):
        req_headers = headers.copy() if headers else {}
        if token is not None:
            req_headers["Authorization"] = f"Bearer {token}"
        self.response = self.get(Endpoints.AUTH_ME, headers=req_headers, **kwargs)
        return self.response

    def saveSession(self, login):
        os.makedirs("test_data/api_data", exist_ok=True)
        with open("test_data/api_data/api_session.json", 'w') as f:
            f.write(json.dumps(login.response.json()))

    def loadSession(self):
        with open("test_data/api_data/api_session.json", 'r') as f:
            self.session.cookies.update(json.load(f)['TOKEN'])
        print("Session loaded successfully")
