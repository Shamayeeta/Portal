from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Prescriptions(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    patient = models.CharField(max_length=200)
    description = models.TextField(default= '')
    email = models.EmailField(max_length=254,null=True)

    def __str__(self):
        return self.patient
    class Meta:
        verbose_name = "prescriptions"
        verbose_name_plural = "prescriptions"