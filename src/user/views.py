from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serializer import UserSerializer
from .tasks import fetch_ip_geolocation_data
from .models import User


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ip_address = request.META.get("REMOTE_ADDR")
        fetch_ip_geolocation_data.delay(ip_address)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("user does not exist")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        return Response({"message": "Success !! You are now logged in"})
