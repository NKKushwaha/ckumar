'''
from django import forms
from app.models import *


class DetailInfoMF(forms.ModelForm):
    class Meta:
        model = DetailInfo
        fields = '__all__'
        #fields = ['name','email']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control mb-2',
                'placeholder' : 'Enter the name'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control mb-2',
                'placeholder' : 'Enter the Email'
            }),
            'mobile' : forms.TextInput(attrs={
                'class' : 'form-control mb-2',
                'placeholder' : 'Enter the Number'
            }),
            'feedback' : forms.Textarea(attrs={
                'class' : 'form-control mb-2',
                'placeholder' : 'Enter the Feedback',
                'rows' : 2
            })
        }


'''