from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    UserID = models.AutoField(primary_key=True)
    StudNo = models.CharField(max_length=45)
    StudName = models.CharField(max_length=45)
    Term = models.CharField(max_length=45)
    Course = models.CharField(max_length=45)
    RefName = models.CharField(max_length=45)
    Username = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)

class AdminInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    AdminNo = models.CharField(max_length=45)
    AdminName = models.CharField(max_length=45)
    Term = models.CharField(max_length=45)
    Course = models.CharField(max_length=45)
    Username = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)