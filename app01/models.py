from django.db import models

# Create your models here.
# from django.db import models
# Create your models here.
class login(models.Model):
    usename = models.CharField(max_length=32)
    password = models.CharField(max_length=32)







