from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from .models import User

# Create your views here.

class CreateUserView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginUserView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email, password=password)

        if not user:
            raise ValueError("Email or password you provide is wrong!")

        