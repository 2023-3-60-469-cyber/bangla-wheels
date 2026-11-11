from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [('buyer', 'Buyer'), ('admin', 'Dealership Admin')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    phone = models.CharField(max_length=20, blank=True)