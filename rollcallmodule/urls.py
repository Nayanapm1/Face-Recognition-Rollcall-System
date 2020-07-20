from django.urls import path
from .import views

app_name='rollcallmodule'

urlpatterns=[
    path('ComparingPage', views.r1),
    path('coursepopup', views.r2),
    path('ExtractingComparing', views.r3),
    path('History', views.r4),
    path('MyAttendace', views.r5),
    path('RollCall', views.r6),
    path('RollCallPage', views.r7),
    path('StudenRecord', views.r8),
]