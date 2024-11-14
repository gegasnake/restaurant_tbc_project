# user/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the user's refresh token from the request
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh token required'}, status=400)

            # Create the RefreshToken object
            token = RefreshToken(refresh_token)

            # Blacklist the token (This will invalidate it)
            token.blacklist()

            return Response({"detail": "Successfully logged out"}, status=200)

        except Exception as e:
            return Response({"detail": str(e)}, status=400)
