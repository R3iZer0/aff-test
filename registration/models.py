from django.db import models



class Lead(models.Model):
    EXPERIENCE_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    country=models.CharField(max_length=100)
    experience = models.CharField(max_length=3, choices=EXPERIENCE_CHOICES)
    created_at = models.DateTimeField(auto_now=True)
