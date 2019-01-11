"""dten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dtenapp.urls')),
    path('attend',include('dtenapp.urls')),
    path('sign',include('dtenapp.urls')),
    path('teacher',include('dtenapp.urls')),
    path('student',include('dtenapp.urls')),
    path('division',include('dtenapp.urls')),
    path('subject',include('dtenapp.urls')),
    path('login',include('dtenapp.urls')),
    path('present',include('dtenapp.urls')),
    path('absent',include('dtenapp.urls')),
    # url(r'^',include('dtenapp.urls')),   
    # url(r'^attend/$',include('dtenapp.urls')),
]

urlpatterns += staticfiles_urlpatterns() 