from django.db import models

# Create your models here.

class Tterm(models.Model):
    ttermid = models.AutoField(primary_key=True)
    ttermname = models.CharField(max_length=100)

    class Meta:
        db_table='Tterm'

class Tcourse(models.Model):
    tcourseid = models.AutoField(primary_key=True)
    tcoursename = models.CharField(max_length=100)

    class Meta:
        db_table='Tcourse'


class TSelectCourse(models.Model):
    tscid = models.AutoField(primary_key=True)
    tterm = models.ForeignKey('Tterm', on_delete=models.CASCADE, db_column='ttermid')
    tcourse = models.ForeignKey('Tcourse', on_delete=models.CASCADE, db_column='tcourseid')
    tstartdate = models.DateField(null=True)
    tenddate = models.DateField(null=True)

    class Meta:
        db_table = 'TSelectCourse'