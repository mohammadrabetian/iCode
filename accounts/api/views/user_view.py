from django.contrib.auth import authenticate, login

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import CreateUserSerializer


class UserView(APIView):
    def post(self, request):
        serialized_data = CreateUserSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data, status=status.HTTP_200_OK)

        return Response(data=serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
