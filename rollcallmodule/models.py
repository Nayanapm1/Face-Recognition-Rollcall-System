from django.db import models
from selectcourse import models as selectcourse_models

# Create your models here.
class attendancerec(models.Model):
    attendanceID = models.AutoField(primary_key=True)
    studetails = models.ForeignKey('studentrec', on_delete=models.CASCADE, db_column='stuid')
    attendetails = models.ForeignKey('attendate', on_delete=models.CASCADE, db_column='attdateid')
    attdatetime = models.DateTimeField(null=True)
    attendance = models.BooleanField(default=True)
    studentphoto = models.CharField(max_length=45)
    term = models.ForeignKey(selectcourse_models.term, on_delete=models.CASCADE, db_column='termid')
    course = models.ForeignKey(selectcourse_models.course, on_delete=models.CASCADE, db_column='courseid')

    class Meta:
        db_table = 'attendancerec'

from django.db import models

class studentrec(models.Model):
    stuid = models.AutoField(primary_key=True)
    stunum = models.CharField(max_length=50)
    stuname = models.CharField(max_length=50)
    selectcourse = models.ForeignKey(selectcourse_models.selectcourse, on_delete=models.CASCADE, db_column='scid')

    class Meta:
        db_table = 'studentrec'

class attendate(models.Model):
    attdateid = models.AutoField(primary_key=True)
    attdate = models.DateTimeField()
    selectcourse = models.ForeignKey(selectcourse_models.selectcourse, on_delete=models.CASCADE, db_column='scid')

    class Meta:
        db_table='attendate'

