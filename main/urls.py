from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name = 'home'),
    path('signIn',views.signin , name='sign_in'),
    path('signUp',views.signup , name='sign_up'),
    path('logout',views.signout , name ='logout'),  
    path('dashboard',views.dashboard , name ='dashboard'),  
]


