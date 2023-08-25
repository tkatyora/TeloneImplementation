from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required , permission_required


# Create your views here.

#CRUD OPERATIONS OF QUOTATION
#1.READ
@login_required(login_url='sign_in') 
def ViewQoute(request):
    content ={}
    content ={
    
   }    
    return render(request,'dashboard.html',content)
#2.CREATE
# @login_required(login_url='sign_in') 
def AddQuote(request):
    if request.method == 'POST':
        form = addQouteForm(request.POST)
        if form.is_valid():
            form.save() 
            mesage= f'Quoatation added succesfully'
            messages.success(request,mesage)
            return redirect('viewE36')
           
        else:
            messages.warning(request, 'Sorry Qoutation not added succesfully')
    else:
        form = addQouteForm()
    content = {}
    content = {
        'form': form,

    }
    return render(request, 'AddQoute.html', content)