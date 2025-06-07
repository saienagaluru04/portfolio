from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField()
    email = models.EmailField()
    phonenumber = models.IntegerField()
    message = models.CharField()
