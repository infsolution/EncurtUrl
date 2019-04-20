# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms 

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255,'placeholder':"Nome"}),
            'email':forms.TextInput(attrs={'class':'form-control', 'maxlength':255,'placeholder':"Email"}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'maxlength':255,'placeholder':"Senha"}),
        }
        error_messages={
            'username':{
                'required':'Campo obrigatório'
            },
            'email':{
                'required':'Campo obrigatório'
            },
            'password':{
                'required':'Campo obrigatório'
            },
        }