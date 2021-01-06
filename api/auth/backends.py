import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')
        try:
            payload = jwt.decode(token, 'SDFSDGVSEGWEGERHEWWT634RY3Y4WG34dua2fy@28^c1^^klpj$+-3ey21aaeds669_', algorithms="HS256")
            user = User.objects.get(username=payload['username'])
            return (user, token)

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')

        return super().authenticate(request)