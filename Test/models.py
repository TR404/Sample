from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100, blank=True, null=True)
    completed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, editable=False)