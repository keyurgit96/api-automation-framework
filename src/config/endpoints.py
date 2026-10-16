class Endpoints:
    # DummyJSON Auth Endpoints (DummyJsonURL)
    AUTH_LOGIN = "/auth/login"
    AUTH_ME = "/auth/me"

    # JSONPlaceholder Posts Endpoints (JsonPlaceholderURL)
    POSTS = "/posts"
    POSTS_ID = "/posts/{id}"

    # Restful API Objects Endpoints (RestfulApiDevURL)
    OBJECTS = "/objects"
    OBJECTS_ID = "/objects/{id}"

    # User / Object Aliases (restapi dev objects used as users in tests)
    USERS = "/objects"
    USERS_ID = "/objects/{id}"

    @staticmethod
    def post_by_id(post_id) -> str:
        return f"/posts/{post_id}"

    @staticmethod
    def object_by_id(object_id) -> str:
        return f"/objects/{object_id}"

    @staticmethod
    def user_by_id(user_id) -> str:
        return f"/objects/{user_id}"
