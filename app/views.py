from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from app.models import *
# from app.forms import *
# Create your views here.
def link(request):
    return render ( request, 'link.html')

def ckumar(request):
    # EDIFO = DetailInfoMF()
    # if request.method == 'POST':
    #     DIFDO = DetailInfoMF(request.POST)
    #     if DIFDO.is_valid():
    #         DIFDO.save()
    #         return render (request, 'index.html')

    if request.method == 'POST':
        print('I am here')
        namev = request.POST['name']
        emailv = request.POST['email']
        mobilev= request.POST['mobile']
        feedbackv = request.POST['feedback']

        DIO = DetailInfo.objects.get_or_create(name = namev, email=emailv, mobile=mobilev, feedback=feedbackv)

        send_mail(
            'From the Google',
            f""" Hii {namev},
                your data is collected successfully""",
            'settings.EMAIL_HOST_USER',
            [emailv],
            fail_silently=False
        ) 

        return render (request, 'index.html', {'success1':True})


    return render (request, 'index.html')





def service (request):
    return render (request, 'service.html')


def about(request):
    return render (request, 'about.html')

def contact(request):

    if request.method == 'POST':
        print('url navigated and submitted')
        first_namev = request.POST['first_name']
        last_namev = request.POST['last_name']
        emailv = request.POST['email']
        phonev = request.POST['phone']
        companyv = request.POST['company']
        urlv = request.POST['url']
        servicev = request.POST['service']
        budgetv = request.POST['budget']
        goalv = request.POST['goal']

        CO = Contactform.objects.get_or_create( first_name = first_namev, last_name=last_namev , email=emailv, phone=phonev, company=companyv,url=urlv, service=servicev, budget=budgetv, goal=goalv)

        return render (request, 'contact.html', {'success':True})
    return render (request, 'contact.html')




def privacy_policy(request):
    return render (request, 'privacy_policy.html')


def terms_and_conditions(request):
    return render (request, 'terms_and_conditions.html')

def refund_policy(request):
    return render (request, 'refund_policy.html')

def gdpr(request):
    return render (request, 'gdpr.html')

