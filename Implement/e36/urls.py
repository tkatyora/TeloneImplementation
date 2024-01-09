from django.urls import path
from . import views

urlpatterns = [
    path('ViewQuotation',views.ViewQoute , name='viewE36'),
    path('ViewMyQuotation',views.ViewMyQoute , name='viewMyE36'),
    path('AddQuotation',views.AddQuote, name = 'addE36'),
    path('E36CreationSteps',views.StepsToFollow, name = 'stepsToFollow'),
    path('WhatIsE36',views.WhatIsE36, name = 'what_is_e36'),
    path('deleteQuotation/<int:pk>',views.DeleteQuote, name = 'DeleteE36'),
    path('updateuotation/<int:pk>',views.updateQuote, name = 'UpdateE36'),
    path('DetailedQuotation/<int:pk>',views.DetailedQuote, name = 'DetailedE36'),
    path('AddDocuments',views.AddDocuments, name = 'AddDocuments'),
    path('viewDocument',views.ViewDocument , name='viewDocuments'),
    path('calculator',views.Calculator , name='Calculator'),
    path('PendingE36',views.PendingQoute , name='pending'),
     path('searchQoute/', views.searchQoute, name='search'),
   
]