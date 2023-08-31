from django import forms
import datetime
from django.forms import ModelForm 
from .models import * 
from django.utils.translation import gettext_lazy as _
print('start')


today_date=datetime.datetime.now().date()

min_date = (today_date - datetime.timedelta(days=1 * 7))
days = (today_date - min_date) 






class addQouteForm(ModelForm):
    Type =forms.ChoiceField(choices=Quotation.name, label='Project Scope',required=True)
    Name =forms.CharField(label='Name of Client',required=True,help_text='Client Who Require Service eg FBC SAMORA MACHEL')
    City =forms.CharField(label='City of Client',required=True,help_text='eg Harare')
    Total = forms.IntegerField(label='Grand Total )',help_text='The Total includes the Materials, Transport, Labour, Wayleaves and Engineering costs')
    Status = forms.ChoiceField(choices=Quotation.status , label='Status of E36' ,help_text='If The E36 is completed Select Completed')
    comment=forms.CharField(label='Add any Comments You Have', required=False, help_text='Write Anything related to the e36(optional) ',
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5, 
                                  }
                              ))
    File = forms.FileField(label= 'Upload The E36', max_length=100, required=True, widget=forms.FileInput(
                                  attrs={
                                       'class':'form-control'
                                  }
                              ))
    DateReceived= forms.DateTimeField(label='Date You Receive The E36', required=True ,widget = forms.DateInput(
     attrs={
         'type':'date',
         'max':today_date ,
        'min':min_date
        }
    ))

    TimeReceived= forms.DateTimeField(label='Time You Receive The E36', required=True ,widget = forms.DateInput(
     attrs={
         'type':'time',
         
        }
    ))
    DateSubmited= forms.DateTimeField(label='Date You Submit The E36', required=True ,widget = forms.DateInput(
     attrs={
         'type':'date',
         'max':today_date ,
        'min':min_date
        }
    ))
    TimeSubmited= forms.DateTimeField(label='Time You Submit The E36', required=True ,widget = forms.DateInput(
     attrs={
         'type':'time',
        }
    ))


    class Meta: 
        model = Quotation
        fields =['File','Name','Type','DateReceived',
         'Receivedfrom','comments','TimeReceived','City',
         'Total','TimeSubmited','DateSubmited','image']
        
        
    