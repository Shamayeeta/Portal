from django.db import models
from django.contrib.auth.models import AbstractUser
import time
import os
# Create your models here

#customized user model
class User(AbstractUser):
    is_doctor= models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)

def content_file_name(instance, filename):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    name, extension = os.path.splitext(filename)
    return os.path.join(instance.user.username, timestr + extension)

#model to store user face image
class UserFaceImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=content_file_name, blank=False)



