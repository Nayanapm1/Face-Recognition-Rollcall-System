from django.urls import path
from .import views

app_name='rollcallmodule'

urlpatterns=[
    path('comparing', views.r1),
    path('coursepopup', views.CoursePopUp),
    path('coursepopup/ok', views.CoursePopUpOk),
    path('ExtractingComparing', views.ExtractingComparingPage),
    path('History', views.r4),
    path('MyAttendance', views.r5),
    path('RollCall', views.r6),
    path('RollCallPage', views.r7),
    path('StudenRecord', views.r8),
    path('StudentInformation', views.ViewStudentInformation),
    path('UploadClassStudentPhoto', views.UploadClassStudentPhoto),
    path('UploadClassStudentPhoto/upload', views.upload),
    path('UploadClassStudentPhoto/reset', views.Udelete),
    path('UploadClassStudentPhoto/proceed', views.Attendancerun),
    path('UploadClassStudentPhoto/upload/proceed', views.Attendancerun),
    path('StudentInformation/importstu',views.importstu)
]