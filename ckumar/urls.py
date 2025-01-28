"""
URL configuration for ckumar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from app.views import *
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ckumar,name='ckumar'),
    path('ckumar/',ckumar,name='ckumar'),
    path('service/',service,name='service'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('privacy_policy/',privacy_policy,name='privacy_policy'),
    path('gdpr/',gdpr,name='gdpr'),
    path('terms_and_conditions/',terms_and_conditions,name='terms_and_conditions'),
    path('refund_policy/',refund_policy,name='refund_policy'),
    path('dashboard/',include('dashboard.urls')),
]
