from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(_("email address"), unique=True)
    username =models.CharField(_("user name"), max_length=255)
    is_active = models.BooleanField(_('is active'), defalt=True)
    is_staff = models.BooleanField(_('is staff'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email