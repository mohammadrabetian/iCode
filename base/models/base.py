import uuid
from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    uuid = models.UUIDField(
        db_index=True, default=uuid.uuid4, editable=False, unique=True
    )

    class Meta:
        app_label = "base"
        abstract = True

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
        self.is_deleted = True
        self.save(update_fields=["deleted_at", "is_deleted"])
