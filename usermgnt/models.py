from django.db import models
from rollcallmodule import models as rollcallmodule_models

# Create your models here.
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)
    StudID = models.ForeignKey(rollcallmodule_models.attendancerec, on_delete=models.CASCADE, db_column='studetails')


    class Meta:
        db_table='user'