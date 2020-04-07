from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)


class FileModel(BaseModel):
    file = models.FileField(upload_to=user_directory_path)
    file_type = models.CharField(max_length=20, null=True, blank=True)
    alt = models.CharField(max_length=20, null=True, blank=True)
