from src.apiClient.api_client import baseAPI
from src.config.endpoints import Endpoints


class userAPI(baseAPI):
    def __init__(self, baseURL=None, session=None):
        super().__init__(baseURL, session)

    def getAllUsers(self, **kwargs):
        self.response = self.get(Endpoints.USERS, **kwargs)
        return self.response.json()

    def getUser(self, user_id, **kwargs):
        self.response = self.get(Endpoints.user_by_id(user_id), **kwargs)
        return self.response.json()

    def createUser(self, payload, **kwargs):
        self.response = self.post(Endpoints.USERS, payload=payload, **kwargs)
        return self.response.json()

    def updateUser(self, user_id, payload, **kwargs):
        self.response = self.put(Endpoints.user_by_id(user_id), payload=payload, **kwargs)
        return self.response.json()

    def deleteUser(self, user_id, **kwargs):
        self.response = self.delete(Endpoints.user_by_id(user_id), **kwargs)
        return self.response.json()

    def patchUser(self, user_id, payload, **kwargs):
        self.response = self.patch(Endpoints.user_by_id(user_id), payload=payload, **kwargs)
        return self.response.json()