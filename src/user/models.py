from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class UserGeolocation(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="geolocation"
    )
    ip_address = models.CharField(max_length=45)
    city = models.CharField(max_length=255, null=True)
    country_code = models.CharField(max_length=2, null=True)
    region = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=255, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    is_vpn = models.BooleanField(null=True)
