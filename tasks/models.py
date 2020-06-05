from django.db import models
from django.contrib.auth.models import User

class task(models.Model):
    title= models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
