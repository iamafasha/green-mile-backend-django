from django.conf import settings
from django.contrib import auth
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import jwt
from .serializers import UserSerializer

from users.models import Worker , Supplier
# Create your views here.



class LoginView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)
            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class AccountType(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        subclass=request.user.subclass
        is_is_hub_manager=False
        if(subclass=='worker'):
            user = Worker.objects.get(username=request.user.username)
            if(user.is_hub_manager):
                subclass='hubmananger'
        return Response({
            'account_type': subclass,
            'is_staff':request.user.is_staff,
            'is_admin':request.user.is_superuser,
            'is_is_hub_manager':is_is_hub_manager,
        }, status=status.HTTP_202_ACCEPTED)