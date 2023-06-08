from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.core.validators import FileExtensionValidator


class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


class Audio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='uploads/',
                            validators=[FileExtensionValidator(allowed_extensions=['wav', 'mp3'])])
