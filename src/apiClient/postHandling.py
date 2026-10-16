from src.apiClient.api_client import baseAPI
from src.config.endpoints import Endpoints


class postAPI(baseAPI):
    def __init__(self, baseURL=None, session=None):
        super().__init__(baseURL, session)

    def getAllPosts(self, **kwargs):
        self.response = self.get(Endpoints.POSTS, **kwargs)
        return self.response.json()

    def getPost(self, post_id, **kwargs):
        self.response = self.get(Endpoints.post_by_id(post_id), **kwargs)
        return self.response.json()

    def createPost(self, payload, **kwargs):
        self.response = self.post(Endpoints.POSTS, payload=payload, **kwargs)
        return self.response.json()

    def updatePost(self, post_id, payload, **kwargs):
        self.response = self.put(Endpoints.post_by_id(post_id), payload=payload, **kwargs)
        return self.response.json()

    def deletePost(self, post_id, **kwargs):
        self.response = self.delete(Endpoints.post_by_id(post_id), **kwargs)
        return self.response.json()

    def patchPost(self, post_id, payload, **kwargs):
        self.response = self.patch(Endpoints.post_by_id(post_id), payload=payload, **kwargs)
        return self.response.json()
