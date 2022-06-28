from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    TEACHER = 'teacher'
    STUDENT = 'student'
    type = models.CharField(max_length=100, choices=((TEACHER, TEACHER), (STUDENT, STUDENT)))
    group = models.CharField(max_length=255, null=True, blank=True)


class Lesson(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    users = models.ManyToManyField(User, related_name="lessons")
    presence = models.BooleanField(default=False)
    mark = models.IntegerField(null=True, blank=True)


class Exam(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    mark = models.IntegerField(null=True, blank=True)
