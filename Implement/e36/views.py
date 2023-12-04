from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required , permission_required
import datetime
from report.views import WeekReportCalculator

count = Quotation.objects.count() 
week = WeekReportCalculator()
print(week)


E36 = Quotation.objects.all().order_by('-created')
Documents = Document.objects.all()
Steps = Document.objects.last()
E36Pending = Quotation.objects.filter(Status='Pending').values().count()
Pending = Quotation.objects.filter(Status='Pending')
# Create your views here.

#CRUD OPERATIONS OF QUOTATION
#1.READ
@login_required(login_url='sign_in') 
def ViewQoute(request):
    content ={}
    content ={
      'E36':E36,
      'count':count
   }    
    return render(request,'viewQoute.html',content)

@login_required(login_url='sign_in') 
def ViewMyQoute(request):
    content ={}
    content ={
      'E36':E36
   }    
    return render(request,'viewMyQuote.html',content)
@login_required(login_url='sign_in') 
def StepsToFollow(request):
    content ={}
    content ={
    'data':Steps
      
   }    
    return render(request,'Steps.html',content)
@login_required(login_url='sign_in') 
def WhatIsE36(request):
    content ={}
    content ={
      
   }    
    return render(request,'WhatIsE36.html',content)
#2.CREATE
@login_required(login_url='sign_in') 
def AddQuote(request):
    if request.method == 'POST':
        form = addQouteForm(request.POST, request.FILES)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.created_by = request.user
            quotation.WeekReport = week
            quotation.save()
           
            mesage= f'Quoatation added succesfully'
            messages.success(request,mesage)
            return redirect('addE36')   
        else:
            messages.warning(request, 'Sorry Qoutation not added succesfully')
    else:
        form = addQouteForm()
    content = {}
    content = {
        'form': form,

    }
    return render(request, 'AddQoute.html', content)
#3.Update
@login_required(login_url='sign_in') 
def updateQuote(request, pk):
    e36_to_update = Quotation.objects.get(id=pk)  # Querry out the Services which much be updated
    if request.method == 'POST':
        form = addQouteForm(request.POST,request.FILES, instance=e36_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'E36 updated succesfully')
            return redirect('viewMyE36')
        else:
            messages.warning(request, 'Sorry E36 not updated ')
    else:
        form = addQouteForm(instance=e36_to_update)
    content = {}
    content = {
        'form':  form,
        'E36Update': e36_to_update

    }
    return render(request, 'updateE36.html', content)
#3.Delete Qoute
@login_required
def DeleteQuote(request, pk):
    e36_to_delete = Quotation.objects.get(id=pk)
    if request.method == 'POST':
        e36_to_delete.delete()
        messages.success(request, 'Quotation Deleted Succefully Succesfully Deleted')
        return redirect('viewMyE36')
    content = {}
    content = {
        'e36_to_delete': e36_to_delete,
        'e36': E36
    }
    return render(request, 'delete.html', content)
#4.View detailed Information
@login_required
def DetailedQuote(request, pk):
    detailed = Quotation.objects.get(id=pk)
    content = {}
    content = {
    'data': detailed,

    }
    return render(request, 'detailed.html', content)
#5.View Pending E36
@login_required(login_url='sign_in') 
def PendingQoute(request):
    if request.method == 'POST':
        form = addQouteForm(request.POST, request.FILES)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.created_by = request.user
            quotation.WeekReport = week
            quotation.save()
           
            mesage= f'Quoatation added succesfully'
            messages.success(request,mesage)
            return redirect('addE36')   
        else:
            messages.warning(request, 'Sorry Qoutation not added succesfully')
    else:
        form = addQouteForm()
    content = {}
    content = {
        'pending': Pending,

    }
    return render(request, 'Pending.html', content)


@login_required(login_url='sign_in') 
def AddDocuments(request):
    if request.method == 'POST':
        form = DocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            Document.Created_by = request.user
            form.save()
            mesage= f'Document added succesfully'
            messages.success(request,mesage)
            return redirect('viewDocuments')   
        else:
            messages.warning(request, 'Sorry AddDocument not added succesfully')
    else:
        form = DocumentsForm()
    content = {}
    content = {
        'form': form,

    }
    return render(request, 'AddDocument.html', content)
def ViewDocument(request):
    content ={}
    content ={
       'Documents': Documents
   } 
    return render(request, 'viewDocument.html', content)
@login_required
def Calculator(request):
    tenpoles = 0
    sevenpoles = 0
    lory = 0
    truck = 0
    transport =0
    if request.method == 'POST':
        Fibre = request.POST.get('fibre')
        transport = request.POST.get('Transport')
        Fibre = 1000
        if Fibre < 10000:
            #use spacing of 50
            poles = Fibre / 50  
        elif Fibre >= 10000 and Fibre <15000:
            #spacing 70
            poles = Fibre / 50
        elif Fibre >15000:
            #spacing 100
            poles = Fibre / 50
        tenpoles = poles / 5
        sevenpoles = poles - tenpoles
        lory = transport*2
        truck = lory * 5
        return redirect('Calculator')
    content = {}
    content = {
       'tenpoles': Fibre,
        'sevenpoles' : sevenpoles,
        'lory' :transport,
        'truck': truck,
    }
       
    return render(request, 'calculator.html', content)


