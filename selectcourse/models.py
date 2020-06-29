from django.db import models

# Create your models here.

class Term(models.Model):
    TermId = models.AutoField(primary_key=True)
    TermName = models.CharField(max_length=45)

    class Meta:
        db_table='Term'

class Course(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=90)

    class Meta:
        db_table='Course'

class SelectCourse(models.Model):
    SelectCourseId = models.AutoField(primary_key=True)
    TermId = models.AutoField(int)
    CourseId = models.AutoField(int)
    StartDate = models.AutoField(Date)
    EndDate = models.AutoField(Date)

    class Meta:
        db_table='Course'