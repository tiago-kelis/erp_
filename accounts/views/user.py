from accounts.views.base import Base
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import User

class GetUser(Base):

    permission_classes = [IsAuthenticated]

    def get(self, resquest) -> None:

        user = User.objects.filter(id=resquest.user.id).first()
        enterprise = self.get_enterprise_user(user)

        serialiser = UserSerializer(user)

        return Response({

            "user": serialiser.data,
            "enterprise": enterprise
        })



