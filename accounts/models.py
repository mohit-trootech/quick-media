from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from accounts.utils.constants import GENDER_CHOICE, PROFILE_UPLOAD_TO

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=1024, null=True, blank=True)
    phone = PhoneNumberField(region="IN", null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, blank=True, null=True)
    profile = models.ImageField(upload_to=PROFILE_UPLOAD_TO, blank=True, null=True)

    def __str__(self):
        return self.username
