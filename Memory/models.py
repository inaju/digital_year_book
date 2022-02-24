from django.db import models
from Account.models import StudentUser
# Create your models here.


class Memory(models.Model):
    StudentID = models.ForeignKey(StudentUser, on_delete=models.DO_NOTHING)
    Description = models.CharField(max_length=255)
    ProfilePic = models.FileField


class HallOfFame(models.Model):
    StudentID = models.ForeignKey(StudentUser, on_delete=models.DO_NOTHING)
    FameTitle = models.FileField
    FameFile = models.CharField(max_length=255)

