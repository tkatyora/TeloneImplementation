from django.shortcuts import render
from e36.models import Quotation

# Create your views here.
import datetime

today_date = datetime.date.today()
start_date = datetime.date(today_date.year, 1, 1) 
min_date = (today_date - datetime.timedelta(days=1 * 8))
def WeekReportCalculator():
    start_date = datetime.date(today_date.year, 1, 1) 
    days = (today_date - start_date ) + datetime.timedelta(days=1 * 10) 
    week = (days // 7).days
    return week

week = WeekReportCalculator()
E36 = Quotation.objects.all().order_by('-created')
# E36 = Quotation.objects.filter(WeekReport=37).values()
E36WEEK = Quotation.objects.filter(WeekReport=week).filter(Status='Completed').values().count()
 
count = Quotation.objects.count() 
def  WeeklyReport(request):
    content ={}
    content ={
    'count':E36WEEK,
    'E36':E36,
    'today': today_date,
    'min':min_date,
    'week':week,
    
}    
    return render(request,'Weekly.html',content)

