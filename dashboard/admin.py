from django.contrib import admin

# Register your models here.
from dashboard.models import *

class SignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
admin.site.register(Signup,SignupAdmin)