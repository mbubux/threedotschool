from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    admin_photo = models.ImageField(upload_to='admin_photos', null=True, blank=True)
    school_logo = models.ImageField(upload_to='school_logos', null=True, blank=True)
