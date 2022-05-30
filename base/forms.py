from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ['user']
        widgets = {
            'complete_date' : DateInput()
        }

    def __init__(self , *args, **kwargs):

        super(TaskForm , self).__init__(*args , **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

        self.fields['complete'].widget.attrs.update({'class': 'form-check-label'})

        self.fields['complete_date'].widget.attrs.update({'class': ''})


class NewUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1' , 'password2']

        def __init__(self , *args,**kwargs):

            super(NewUserCreationForm,self).__init__(*args , **kwargs)

            for name , field in self.fields.items():
                field.widget.attrs.update({'class':'form-control'})
