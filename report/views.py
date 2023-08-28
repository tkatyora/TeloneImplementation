from django.shortcuts import render
import datetime
from e36.models import *

# Create your views here.
today_date=datetime.datetime.now().date()
start_date = (today_date - datetime.timedelta(days=1 * 339))
min_date = (today_date - datetime.timedelta(days=1 * 7))
days = (today_date - start_date) // 7
weeks = str(days).split('days',1)[0]
E36 = Quotation.objects.all()    
def  WeeklyReport(request):
    content ={}
    content ={
    'E36':E36,
    'today': today_date,
    'min':min_date,
    'week':weeks
}    
    return render(request,'Weekly.html',content)