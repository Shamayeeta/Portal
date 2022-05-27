from django.db import models
from django.contrib.auth import get_user_model
from matplotlib import image
User = get_user_model()
# Create your models here.
# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.username, filename)

# class Database(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=user_directory_path)
#     def __str__(self):
#      return self.username