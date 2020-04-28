from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status

from accounts.models import User



@api_view(http_method_names=["PUT"])
def set_password(request):
    id = request.data.get("user_id")
    password = request.data.get("password")
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(data={"result": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    password = make_password(password)
    user.password = password
    user.save()
    return Response(data={"result": "Password Changed Successfuly"}, status=status.HTTP_200_OK)