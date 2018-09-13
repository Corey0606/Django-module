from django.db import models

# Create your models here.
# from django.db import models
# Create your models here.

class login(models.Model):
    # nid = models.AutoField(primary_key=True)
    usename = models.CharField(max_length=32)
    password=models.CharField( max_length=32)
    # age=models.IntegerField()

class book(models.Model):
    title = models.CharField(max_length=32)
    publish = models.CharField(max_length=32)
    price = models.IntegerField(max_length=10)






