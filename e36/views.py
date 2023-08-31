from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required , permission_required

E36 = Quotation.objects.all().order_by('-DateReceived')
# Create your views here.

#CRUD OPERATIONS OF QUOTATION
#1.READ
# @login_required(login_url='sign_in') 
def ViewQoute(request):
    content ={}
    content ={
      'E36':E36
   }    
    return render(request,'viewQuote.html',content)
def StepsToFollow(request):
    content ={}
    content ={
      
   }    
    return render(request,'Steps.html',content)
def WhatIsE36(request):
    content ={}
    content ={
      
   }    
    return render(request,'WhatIsE36.html',content)
#2.CREATE
# @login_required(login_url='sign_in') 
def AddQuote(request):
    if request.method == 'POST':
        form = addQouteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            Quotation.user = request.user
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

def DeleteQuote(request, pk):
    e36_to_delete = Quotation.objects.get(id=pk)
    if request.method == 'POST':
        e36_to_delete.delete()
        messages.success(request, 'Quotation Deleted Succefully Succesfully Deleted')
        return redirect('viewE36')
    content = {}
    content = {
        'e36_to_delete': e36_to_delete,
        'e36': E36
    }
    return render(request, 'delete.html', content)
