from rest_framework.authentication import TokenAuthentication as BaseAutenticate

class TokenAuthenticate(BaseAutenticate):
    keyword = "Bearer"