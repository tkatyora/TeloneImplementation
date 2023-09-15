from django import forms
from django.forms import ModelForm 
from .models import * 
from django.utils.translation import gettext_lazy as _
import datetime

today_date = datetime.date.today()



min_date = (today_date - datetime.timedelta(days=1 * 7))
days = (today_date - min_date) 


class addQouteForm(ModelForm):
    Type =forms.ChoiceField(choices=Quotation.name, label='Project Scope',required=True)
    NameClient =forms.CharField(label='Name of Client',help_text='Client Who Require Service eg FBC SAMORA MACHEL')
    City =forms.CharField(label='City of Client',required=True,help_text='eg Harare')
    Total = forms.DecimalField(label='Grand Total )', max_digits=10, decimal_places=2,help_text='The Total includes the Materials, Transport, Labour, Wayleaves and Engineering costs',required=False)
    Status = forms.ChoiceField(choices=Quotation.status , label='Status of E36' ,help_text='If The E36 is completed Select Completed',required=True)
    comment=forms.CharField(label='Add any Comments You Have', required=False, help_text='Write Anything related to the e36(optional) ',
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5, 
                                  }
                              ))
    File = forms.FileField(label= 'Upload The E36',required=False, max_length=100,  widget=forms.FileInput(
                                  attrs={
                                       'class':'form-control'
                                  }
                              ))
    DateReceived= forms.DateTimeField(label='Date You Receive The E36', required=False ,widget = forms.DateInput(
     attrs={
         'type':'date',
         'max':today_date ,
        'min':min_date
        }
    ))

    # TimeReceived= forms.TimeField(label='Time You Receive The E36', required=False
    # )
    DateSubmited= forms.DateTimeField(label='Date You Submit The E36', required=False ,widget = forms.DateInput(
     attrs={
         'type':'date',
         'max':today_date ,
        'min':min_date
        }
    ))
    # TimeSubmited= forms.TimeField(label='Time You Submit The E36', required=False ,widget = forms.TimeInput(
    #  attrs={
    #      'type':'time',
    #     }
    # ))


    class Meta: 
        model = Quotation
        fields =['File','NameClient','Type','DateReceived',
         'Receivedfrom','comments','TimeRecived','City',
         'Total','TimeSubmitted','DateSubmited','survey','Status','WeekReport']
        
        
    


class DocumentsForm(ModelForm):
    Name =forms.CharField(label='Document Name',required=True)
    Discription=forms.CharField(label='The Purpose of The Document', required=False,
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5, 
                                  }
                              ))
    File = forms.FileField(label= 'Upload The Document', max_length=200, required=True, widget=forms.FileInput(
                                  attrs={
                                       'class':'form-control'
                                  }
                              ))
    
    class Meta: 
        model = Document
        fields =['File','Name','Discription']
        
        
    