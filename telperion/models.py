from django.db import models
from django.contrib.auth.models import User as OriginalUser


class School(models.Model):
    schoolname = models.CharField(max_length=100)
    def __unicode__(self):
        return self.schoolname



class User(models.Model):
    user = models.ForeignKey(OriginalUser, unique=True)
    schools = models.ManyToManyField(School)



class Question(models.Model):
    questiontext = models.CharField(max_length=400)
    school = models.ForeignKey(School)

class Essay(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=5000)
    user = models.ForeignKey(User)


