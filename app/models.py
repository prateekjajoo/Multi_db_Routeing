from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#


class UserRole(User):
    """ User model inherited by django.contrib.auth.models.User """

    db_assign = models.CharField(max_length=150, default='None', null=True, blank=True)


class Product(models.Model):
    """Create product model """
    user = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    prize = models.IntegerField()
