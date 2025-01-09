from django.contrib import admin
from app.models import *
# Register your models here.

class cust(admin.ModelAdmin):
    list_display = ['name','email','mobile','feedback']
    list_display_links = ['email']
    list_editable = ['name']
    search_fields = ['name']
    # list_filter = ['email','name']





admin.site.register(DetailInfo,cust)




class Contactf(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'company',  'url', 'service', 'budget', 'goal']
    list_display_links = ['email','url']
    search_fields = ['first_name','last_name','email','url']


admin.site.register(Contactform,Contactf)


