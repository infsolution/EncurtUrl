# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms 

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255,'placeholder':"Escolha um nome só seu"}),
            'email':forms.TextInput(attrs={'class':'form-control', 'maxlength':255,'placeholder':"Informe seu melhor email"}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'maxlength':255,'placeholder':"Crie uma senha"}),
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