from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import *
from app.models import *
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        signupLO = Signup.objects.filter(email=email, password=password)
        if signupLO:
            return render(request, 'display.html')
        else:
            return render(request, 'login.html',{'invalid':True})

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            signupSO = Signup.objects.get_or_create(name=name, email=email, password=password)
            if signupSO:
                return render(request, 'login.html')
            else:
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html', {'password_not_match':True})

    return render(request, 'signup.html')

def display(request):
    Ob = DetailInfo.objects.all()
    return render(request,'display.html',{'OB':Ob})