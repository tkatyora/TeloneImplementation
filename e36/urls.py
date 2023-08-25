from django.urls import path
from . import views

urlpatterns = [
    path('ViewQuotation',views.ViewQoute , name='viewE36'),
    path('AddQuotation',views.AddQuote, name = 'addE36'),
]