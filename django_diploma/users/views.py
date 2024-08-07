import json

from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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

        # serializer = SignInSerializer(data=request.data)
        # if serializer.is_valid():
        #     user = serializer.validated_data['user']
        #     refresh = RefreshToken.for_user(user)
        #     return Response({
        #         'refresh': str(refresh),
        #         'access': str(refresh.access_token),
        #     }, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
