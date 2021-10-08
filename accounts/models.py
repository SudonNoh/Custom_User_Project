from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from .managers import UserManager
from Core.models import TimeStampedModel

import jwt

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    username = models.CharField(db_index=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    user_code = models.CharField(max_lenght=5, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_code']

    objects = UserManager()
    
    def __str__(self):
        return self.email