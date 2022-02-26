from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200, blank=True)
    notification = models.BooleanField(default=True, blank=True)
    stocks = models.TextField(max_length=1000, blank=True)
    nudgedata = models.JSONField(null=True)

    def __str__(self):
        return f" {self.id}: {self.user} {self.notification} {self.stocks} {self.nudgedata}"

