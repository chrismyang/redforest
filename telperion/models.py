from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)


class School(models.Model):
    user = models.ForeignKey(User)
    schoolname = models.CharField(max_length=100)

class Essay(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=5000)
    school = models.ForeignKey(School)