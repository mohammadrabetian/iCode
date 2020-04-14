from django.db import models

from base.models import BaseModel
from accounts.models import User



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)


class FileModel(BaseModel):
    file = models.FileField(upload_to=user_directory_path)
    file_type = models.CharField(max_length=20, null=True, blank=True)
    alt = models.CharField(max_length=20, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="files")

    class Meta:
        app_label = "base"
