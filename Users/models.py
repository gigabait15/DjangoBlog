from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import NULLABLE


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

