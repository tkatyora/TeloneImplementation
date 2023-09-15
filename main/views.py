from django.shortcuts import render, redirect
from .models import *
from e36.models import *
from .forms import *
from .decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
# collecting The Data from Database
E36 = Quotation.objects.all().order_by('-DateReceived')
contact = Contacts.objects.all()
first_slide = home.objects.first()
second_slide = home.objects.all()[1:1]
last_slide = home.objects.last()
@unauthenticated_user
def home(request):
    content ={}
    content ={
        'second_slide' : second_slide,
        'first_slide': first_slide,
        'last_slide': last_slide,
    }
    return render(request , 'index.html' , content)



@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        userForm = CreateUser(request.POST)
        if userForm.is_valid():
            user = userForm.save()
            username = userForm.cleaned_data.get('username')
            message = 'Account for',{username},'have been succesfully created'
            messages.success(request,message )
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request,'User Form Is Not Valid' )
            return redirect('sign_up')           
    else:
        userForm = CreateUser()
        
    content={}
    content = {
        'form' : userForm , }
    return render(request, 'regester.html' , content)


@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request , username = username , password = password)
        if User is not None:
            login(request, User)
            messages.success(request, 'Log  Successfully')
            return redirect('dashboard') 
        else:
            messages.warning(request, 'Invalid Username and  Paasword')
            return redirect('sign_in')
                      
    return render(request, 'login.html' )

@login_required(login_url='sign_in') 
def signout(request):
    logout(request)
    messages.success(request, 'Log Out successfully')
    return redirect('sign_in')


#dashaboard

def dashboard(request):
    content ={}
    content ={
    'E36':E36
    }  
    return render(request , 'mainDashboard.html',content)

#For Conducts
def contacts(request):
    content = {}
    content={
        'contacts': contact
    }
    return render(request , 'contacts.html',content)

def addConducts(request):
    if request.method == 'POST':
        contactForm = AddContactForm(request.POST)
        if  contactForm.is_valid():
            form = contactForm.save()
            return redirect('contacts') 
        else:
            messages.warning(request,'User Form Is Not Valid' )
                    
    else:
       contactForm = AddContactForm()
        
    content={}
    content = {
        'form' : contactForm }
   
    return render(request , 'addcontact.html',content)