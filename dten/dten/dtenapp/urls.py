from django.conf.urls import url
from .import views
from django.urls import path

urlpatterns = [
    # url(r'^',views.index),
    # url(r'^attend/$',views.attend),
    path('',views.index),
    path('attend',views.attend),
    path('sign',views.sign),
    path('teacher',views.teacher),
    path('student',views.student),
    path('division',views.division),
    path('subject',views.subject),
    path('stddata',views.student),
    path('login',views.login),
    path('present',views.present),
    path('absent',views.absent),
]