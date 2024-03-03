from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.CharField(max_length=20, unique=True)
    user_status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user_id


class Tag(models.Model):
    tag_id = models.CharField(max_length=100, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    tag_status = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_id


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='logs', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    event = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.time}: {self.user.user_id} - {self.tag.tag_id}'