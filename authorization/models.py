from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser

# custom model for User


class User(AbstractUser):
    # No requirement mentioned for this field type. so making it char field
    author_pseudonym = models.CharField(max_length=64, null=True, blank=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
