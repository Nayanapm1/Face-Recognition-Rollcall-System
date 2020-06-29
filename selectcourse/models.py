from django.db import models

# Create your models here.
class Term(models.Model):
    TermId = models.AutoField(primary_key=True)
    TermName = models.CharField(max_length=45)

class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    Course = models.CharField(max_length=60)

class SelectCourse(models.Model):
    CourseID = models.IntegerField(max_length=10)
    TermID = models.IntegerField(max_length=10)
    SatrtDate = models.DateField(max_length=45)
    EndDate = models.DateField(max_length=45)

