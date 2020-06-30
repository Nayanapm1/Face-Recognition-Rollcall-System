from django.db import models


# Create your models here.
class History(models.Model):
    Attendance = models.CharField(max_length=45)
    AttendanceID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=45)
    Date = models.DateField(max_length=45)
    Password = models.CharField(max_length=45)
    StudentName = models.CharField(max_length=45)
    StudentNo = models.CharField(max_length=45)
    TermName = models.CharField(max_length=45)
    Username = models.CharField(max_length=45)

    class Meta:
        db_table = 'History'

from django.db import models

# Create your models here.
