from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage, default_storage
from .models import attendancerec, studentrec, attendate
from selectcourse.models import term, course, selectcourse
import pandas as pd
import os
import datetime as d
#import pymysql

import os
from rollcallmodule.Attendance import *

from flask import Flask, request, render_template

# Create your views here.

def r1(request):
    return render(request, 'ComparingPage.html')

def CoursePopUp(request):
    termlist=term.objects.all()
    context={'termlist':termlist}
    return render(request, 'coursepopup.html', context)

def CoursePopUpOk(request):
    if request.method == "POST":
        request.session['termid'] = request.POST.get('term')
        request.session['courseid'] = request.POST.get('course')
        request.session['date'] = request.POST.get('date')
        print (request.session.items())
        return HttpResponse(status=204)

def ExtractingComparingPage(request):
    tid = request.session['termid']
    cid = request.session['courseid']
    attdlist = attendancerec.objects.all().filter(term=tid, course=cid)
    context = {'attdlist': attdlist}
    return render(request, 'ExtractingComparing.html', context)

def r4(request):
    return render(request, 'History.html')

def r5(request):
    return render(request, 'MyAttendancePage.html')

def r6(request):
    return render(request, 'RollCall.html')

def r7(request):
    return render(request, 'RollCallPage.html')

def r8(request):
    return render(request, 'StudenRecord.html')

def ViewStudentInformation(request):
    return render(request, 'UploadStudentInformationPage.html')


# def ExtractData(request,attid):
#     # if request.method== "POST":
#     #     attrecord = attendancerec.objects.get(attendanceID=attid)
#     #     print(attrecord)
#     #     term1.termname=request.POST.get('txtTerm'+str(tid))
#     #     term1.save()
#     #     return HttpResponseRedirect('/sc/term')

def UploadClassStudentPhoto(request):
    return render(request, 'UploadClassStudentPhotoPage.html')

def upload(request):
    fileitems = request.FILES.getlist('filename')
    print(fileitems)
    fs = FileSystemStorage(location='rollcallmodule/StudentUplaodedImages/')
    for fileitem in fileitems:
        fs.save(fileitem.name, fileitem)
    return render(request, 'UploadClassStudentPhotoPage.html')

def Attendancerun(request):
    matchedIds = Run()
    #matchedIds =  {'2020A001': 63, '2020A011': 49}
    tid = request.session['termid']
    cid = request.session['courseid']
    date = request.session['date']
    tt = term.objects.get(termid=tid)  # Comes term selection
    cc = course.objects.get(courseid=cid)  # Comes course selection
    #ad = attendate.objects.get(attdatetime=did)  # Comes date selection
    for id, perc in matchedIds.items():
        std = studentrec.objects.filter(stunum=id)
        if len(std)!=0:
            attd = attendancerec.objects.filter(studetails=std[0], term=tt, course=cc)
            if len(attd)==0:
                attd = attendancerec()
                attd.studetails = std[0]
                attd.attdatetime = date
                #attd.attendetails = ad
                attd.attendance = True if perc > 60 else False
                attd.matchrate = perc
                attd.term = tt
                attd.course = cc
            else:
                attd = attendancerec.objects.get(studetails=std[0],term=tt, course=cc)
                attd.attdatetime = datetime.now()
                attd.attendance = True if perc > 60 else False
                attd.matchrate = perc
            attd.save()

    unmatched = studentrec.objects.filter(selectcourse__term=tt, selectcourse__course=cc).exclude(stunum__in=matchedIds.keys())
    for ustd in unmatched:
        attd = attendancerec.objects.filter(studetails=ustd, term=tt, course=cc)
        if len(attd)==0:
            attd = attendancerec()
            attd.studetails = ustd
            attd.attdatetime = datetime.now()
            #attd.attendetails = ad
            attd.attendance = False
            attd.term = tt
            attd.course = cc
            attd.save()

    return HttpResponseRedirect('/rollcallmodule/ExtractingComparing')

def Udelete(request):
#     # fileitem = request.FILES['filename']
#     # print(fileitem)
#     # fs = FileSystemStorage(location='rollcallmodule/StudentUplaodedImages/')
#     # fs.delete(fileitem.name, fileitem)
        return render(request, 'UploadClassStudentPhotoPage.html')

    # check if the file has been uploaded
    #if fileitem.filename:
        # strip the leading path from the file name
        #fn = os.path.basename(fileitem.filename)
        # open read and write the file into the server
        #open(fn, 'wb').write(fileitem.file.read())

    #app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# def upload(request1):
#     target = os.path.join(APP_ROOT, 'UploadedImages/')
#     print(target)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#
#     for file in request.files.getlist("file"):
#         print(file)
#         filename = file.filename
#         destination = "/".join([target, filename])
#         print(destination)
#         file.save(destination)
#         print("Upload Complete")
#     return render_template("UploadClassStudentPhotoPage.html")

#def UploadStudentInformation(request):
 #   if request.method== "POST":
 #       studentrec1 = studentrec()
 #       studentrec1.stunum=request.POST.get('stunum')
  #      studentrec1.stuname = request.POST.get('stuname')
  #      studentrec1.selectcourse = request.POST.get('scid')
  #      studentrec1.save()
   #     return HttpResponseRedirect('/rollcallmodule/StudentInformation')

def getext(filename):
    strlist=filename.split('.')
    return strlist[len(strlist)-1]

def importstu(request):
    if request.method == "POST":
        files = request.FILES.getlist('filename')
        print(files)
        for file in files:
            type_excel = getext(file.name)
            print(type_excel)
            if 'xlsx' == type_excel or 'xls'==type_excel:
                filename=pd.read_excel(file)
                rows=len(filename)
                # termid=request.session.get('termid')
                # courseid=request.session.get('courseid')
                # term1 = term.objects.get(termid=termid)
                # course1 = course.objects.get(courseid=courseid)
                # sc=selectcourse.objects.filter(scid=scid,course=course1)
                for i in range(rows):
                    stunum=filename['stunum'][i]
                    stuname=filename['stuname'][i]
                    scid1 = filename['scid'][i]
                    sc = selectcourse.objects.get(scid=scid1)
                    student = studentrec()
                    student.stunum=stunum
                    student.stuname=stuname
                    student.selectcourse=sc
                    student.save()
        return HttpResponseRedirect('/rollcallmodule/StudentInformation')