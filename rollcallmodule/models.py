from django.db import models
from selectcourse import models as selectcourse_models
import datetime as d


# Create your models here.

class studentrec(models.Model):
    stuid = models.AutoField(primary_key=True)
    stunum = models.CharField(max_length=50)
    stuname = models.CharField(max_length=50)
    selectcourse = models.ForeignKey(selectcourse_models.selectcourse, on_delete=models.CASCADE, db_column='scid')

    class Meta:
        db_table = 'studentrec'

    # def getrate(self):
    #     attdate = attendate.objects.filter(selectcourse=self.selectcourse)
    #     attlist = []
    #     rate = "0%"
    #     attendlist = []
    #     for row in attdate:
    #         attdateid = row.attdateid
    #         attrec = attendancerec.objects.filter(attendetails=row, studetails=self)
    #         attendrec = attendancerec.objects.filter(attendetails=row, studetails=self, attendance=1)
    #
    #         if attrec.count() != 0:
    #             attlist.append(attrec[0])
    #         if attendrec.count() != 0:
    #             attendlist.append(attendrec[0])

        # if attdate.count() != 0:
        #     totalcount = attdate.count()
        #     acount = len(attendlist)
        #     if totalcount != 0:
        #         acrate = acount / totalcount
        #         acrate = '%.2f%%' % (acrate * 100)
        # return acrate

class attendate(models.Model):
    attdateid = models.AutoField(primary_key=True)
    attdate = models.DateTimeField()
    selectcourse = models.ForeignKey(selectcourse_models.selectcourse, on_delete=models.CASCADE, db_column='scid')

    class Meta:
        db_table='attendate'

    # def StartNewDate(scid):
    #     nowtime = d.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     attdate = attendate()
    #     attdate.attdate = nowtime
    #
    #     sc = selectcourse_models.objects.get(scid=scid)
    #     attdate.selectcourse = sc
    #     attdate.save()
    #     attdateid = attdate.attdateid
    #     return attdateid

    def getmaxid(scid):
        sql="select * from attendate where selectcourse="+str(scid.scid)+" order by attdate desc limit 1"
        lastdate=attendate.objects.raw(sql)
        attdateid=lastdate[0].attdateid
        return attdateid


class attendancerec(models.Model):
    attendanceID = models.AutoField(primary_key=True)
    studetails = models.ForeignKey('studentrec', on_delete=models.CASCADE, db_column='stuid')
    attendetails = models.ForeignKey('attendate', on_delete=models.CASCADE, db_column='attdateid')
    attdatetime = models.DateField(null=True)
    attendance = models.BooleanField(default=True)
    studentphoto = models.CharField(max_length=45)
    term = models.ForeignKey(selectcourse_models.term, on_delete=models.CASCADE, db_column='termid')
    course = models.ForeignKey(selectcourse_models.course, on_delete=models.CASCADE, db_column='courseid')

    class Meta:
        db_table = 'attendancerec'

    def atthist(scid, attdateid):
        scid = selectcourse_models.objects.get(scid=scid)
        attdatelist = attendate.objects.filter(selectcourse=scid)
        if attdateid == 0:
            attdateid = attendate.getmaxid(scid)
            attdate = attendate.objects.get(attdateid=attdateid)
            attlist = attendancerec.objects.filter(attendetails=attdate)
        else:
            attdate = attendate.objects.get(attdateid=attdateid)
            attlist = attendancerec.objects.filter(attendetails=attdate)
        context = {'attdatelist': attdatelist, 'attreclist': attlist, 'attdateid': attdateid}
        return context

    def stats(attdateid):
        attdate = attendate.objects.get(attdateid=attdateid)
        total = attendancerec.objects.filter(attendetails=attdate)
        attended = attendancerec.objects.filter(attendetails=attdate, attendance=1)
        if total.count() == 0:
            rate = "0%"
        else:
            rate = attended.count() / total.count()
            rate = '%.2f%%' % (rate * 100)

        stats = {'total': total.count(), 'attended': attended.count(), 'rate': rate}
        return stats
