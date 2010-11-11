from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    schools = models.ManyToManyField(School)

class School(models.Model):
    schoolname = models.CharField(max_length=100)


class Essay(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=5000)
    user = models.ForeignKey(User)


class Question(models.Model):
    questiontext = models.CharField(max_length=200)
    school = models.ForeignKey(School)
