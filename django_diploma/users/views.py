import json
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse

from .serializers import SignInSerializer, SignUpSerializer, ProfileSerializer
from .models import Profile


class SignUpView(APIView):
    def post(self, request):
        try:
            user_data = json.loads(request.body)
            username = user_data.get("username")
            password = user_data.get("password")
            first_name = user_data.get("first_name")

            if not username or not password or not first_name:
                return JsonResponse({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, password=password, first_name=first_name)
            return JsonResponse({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignInApiView(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        username = user_data.get("username")
        password = user_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignOutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "User signed out successfully"}, status=status.HTTP_200_OK)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
