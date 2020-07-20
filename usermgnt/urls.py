from django.urls import path
from . import views

app_name = 'usermgnt'

urlpatterns=[
    path('student', views.StudLogin),
    path('admin', views.AdminLogin),
    path('student/login', views.SLoginAction),
    path('admin/login', views.ALoginAction)
]