from django.urls import path
from .import views

app_name='rollcallmodule'

urlpatterns=[
    path('ComparingPage', views.r1),
    path('coursepopup', views.r2),
    path('ExtractingComparing', views.r3),
    path('History', views.r4),
    path('MyAttendance', views.r5),
    path('RollCall', views.r6),
    path('RollCallPage', views.r7),
    path('StudenRecord', views.r8),
    path('StudentInformation', views.ViewStudentInformation),
    path('UploadClassStudentPhoto', views.UploadClassStudentPhoto),
    path('UploadClassStudentPhoto/upload', views.upload),
    path('UploadClassStudentPhoto/proceed', views.Attendancerun)
]