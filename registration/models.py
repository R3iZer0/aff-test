from django.db import models


class Lead(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    country=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
