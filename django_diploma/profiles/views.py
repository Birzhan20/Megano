from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Avatar
from .serializers import ProfileSerializer, PasswordSerializer, AvatarSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60*10), name='dispatch')
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            profile = request.user.profile
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        try:
            profile = request.user.profile
            serializer = ProfileSerializer(profile, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)


class PasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            profile = request.user.profile  # Предполагается, что профиль связан с пользователем через OneToOneField
            serializer = PasswordSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'Password updated successfully.'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)


class AvatarAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            profile, created = Profile.objects.get_or_create(user=request.user)
            if "avatar" in request.FILES:
                if hasattr(profile, 'avatar'):
                    avatar = profile.avatar
                    avatar.src = request.FILES["avatar"]
                    avatar.save()
                else:
                    avatar = Avatar.objects.create(profile=profile, src=request.FILES["avatar"])

                serializer = AvatarSerializer(avatar)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found and could not be created.'},
                            status=status.HTTP_404_NOT_FOUND)
