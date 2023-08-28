from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUser
from .decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required
from django.contrib.auth.models import User

# Create your views here.
# collecting The Data from Database

second_slide = home.objects.get(id='2')
first_slide = home.objects.get(id='1')
last_slide = home.objects.get(id='3')
# @unauthenticated_user
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
            return redirect('sign_up') 
        # else:
        #     messages.warning(request, 'Invalid Username and  Paasword/nPlease Try again')
        #     return redirect('dashboard')
                      
    return render(request, 'login.html' )

@login_required(login_url='sign_in') 
def signout(request):
    logout(request)
    messages.success(request, 'Log Out successfully')
    return redirect('sign_in')


#dashaboard

def dashboard(request):
    return render(request , 'mainDashboard.html')

