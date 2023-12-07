from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class ConfirmCode(models.Model):
    code = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
