from django.urls import path
from . import views

urlpatterns = [
    path('ViewQuotation',views.ViewQoute , name='viewE36'),
    path('AddQuotation',views.AddQuote, name = 'addE36'),
    path('E36CreationSteps',views.StepsToFollow, name = 'stepsToFollow'),
    path('WhatIsE36',views.WhatIsE36, name = 'what_is_e36'),
    path('deleteQuotation/<int:pk>',views.DeleteQuote, name = 'DeleteE36'),
    path('updateuotation/<int:pk>',views.AddQuote, name = 'UpdateE36'),
]