from django.db import models
from rollcallmodule import models as rollcallmodule_models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        db_table='user'

class MyAttendance(models.Model):
    myattendanceid = models.AutoField(primary_key=True)
    studnum = models.ForeignKey(rollcallmodule_models.attendancerec, on_delete=models.CASCADE, db_column='studetails')

    class Meta:
        db_table='attendance'