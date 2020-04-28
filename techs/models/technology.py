from django.db import models

from base.models import BaseModel


class Technology(BaseModel):
    
    class Meta:
        app_label = "techs"