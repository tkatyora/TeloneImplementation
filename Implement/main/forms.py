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
   
    #Ecnum = forms.IntegerField(label ='Enter Your EC Number', required=False)
    class Meta:
        model = User
        fields = ['first_name', 'username','email','password1','password2'] 



class AddContactForm(ModelForm):
   
    Name = forms.CharField( label='Enter  Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
  
    Extension = forms.CharField( label='Enter Extension',
                                widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    Department = forms.CharField( label='Enter Department or Location',
                              widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                     
                                  }))
   
   
    class Meta:
        model = Contacts
        fields = ['Name', 'Extension','Department'] 