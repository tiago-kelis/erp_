from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from rest_framework.response import Response

class Signup(Base):
    def post(self, request) -> None:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        user = Authentication.signup(self, name=name, email=email, password=password)

        seralizer = UserSerializer(user)

        return Response({"user": seralizer.data})


