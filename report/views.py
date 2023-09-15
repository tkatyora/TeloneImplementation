from django.shortcuts import render
from e36.models import *

# Create your views here.
import datetime

today_date = datetime.date.today()
start_date = datetime.date(today_date.year, 1, 1) 
# start_date = (today_date - datetime.timedelta(days=1 * 250))
min_date = (today_date - datetime.timedelta(days=1 * 7))
days = (today_date - start_date) 
week = days // 7
print(start_date)
print(week)
print(days)
weeks = str(days).split('days',1)[0]
E36 = Quotation.objects.all().order_by('-created')
# E36 = Quotation.objects.filter(WeekReport=37).values()
E36WEEK = Quotation.objects.filter(WeekReport=37).values().count()
 
count = Quotation.objects.count() 
def  WeeklyReport(request):
    content ={}
    content ={
    'count':E36WEEK,
    'E36':E36,
    'today': today_date,
    'min':min_date,
    'week':weeks,
    
}    
    return render(request,'Weekly.html',content)

