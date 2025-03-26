from django.contrib import admin
from django.urls import path
from dashboard.views import *

urlpatterns = [ 
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('display/',display,name='display'),
]