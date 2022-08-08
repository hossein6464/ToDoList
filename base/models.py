from pickle import FALSE, TRUE
import re
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=TRUE, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=FALSE)
    create = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.title

    class Meta:
        ordering = ['complete']    