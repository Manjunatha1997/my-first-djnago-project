from django.db import models

# Create your models here.

class Courses(models.Model):
    name=models.CharField(max_length=100)
    teacher=models.CharField(max_length=100)
    duration=models.IntegerField()


class Portfolio(models.Model):
    img=models.ImageField(upload_to='portfolio')
    name=models.CharField(max_length=100)
    qual=models.CharField(max_length=100)
    email=models.EmailField()



