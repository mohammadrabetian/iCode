from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import CreateUserSerializer, GetUserSerializer
from accounts.models import User


class UserView(APIView):
    def post(self, request):
        serialized_data = CreateUserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data, status=status.HTTP_200_OK)
        return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        limit = int(request.GET.get("limit", "10"))
        page = int(request.GET.get("page", "1"))
        artists = User.objects.all()
        pages = Paginator(artists, limit)
        page=pages.page(page)
        serialized_data = GetUserSerializer(page , many=True)
        return Response (serialized_data.data, status=status.HTTP_200_OK)
