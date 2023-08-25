from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUser(UserCreationForm):
   
    first_name = forms.CharField(required=True , label='Enter First Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
  
    username = forms.CharField(required=True , label='Enter Username',
                                widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    email = forms.EmailField(required=True , label='Enter Email',
                              widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                     
                                  }))
   

    class Meta:
        model = User
        fields = ['first_name', 'username','email','password1','password2'] 