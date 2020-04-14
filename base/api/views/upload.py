from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

from base.models import FileModel


@require_http_methods(['POST'])
def upload(request: HttpRequest) -> JsonResponse:
    file = request.FILES.get('file')
    user = request.user

    if not file:
        return JsonResponse(data={"result": "File Not Found"})
    
    if int(file.size) > settings.UPLOAD_MAX_SIZE:
        return JsonResponse(data={"result": "File Larger Than Allowed"}, status=400)

    file_object = FileModel()

    if not user.is_anonymous:
        file_object.user = request.user

    file_object.file = file
    file_object.type = file.content_type
    file_object.name = file.name
    file_object.save()

    data = {}
    data["url"] = file_object.file.url
    return JsonResponse(data={"data": data}, status=200)
