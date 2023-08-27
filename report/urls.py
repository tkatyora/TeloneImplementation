from django.urls import path
from . import views

urlpatterns = [

    path('Weekly',views.WeeklyReport, name = 'weekly'),
]