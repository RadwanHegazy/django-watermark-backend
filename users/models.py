from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from datetime import datetime

class User (AbstractUser):
    username = None
    groups = None
    first_name = None
    last_name = None


    full_name = models.CharField(_('Full Name'),max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    is_gold = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

