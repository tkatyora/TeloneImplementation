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
    Type =forms.ChoiceField(choices=Quotation.name, label='Select the Type of Srvice',required=True,help_text='E36 for GPON , Radio are not made at this Department')
    Name =forms.CharField(label='Enter Name of E36',required=True,help_text='The Name Of The Client Who Requre Service eg FBC SAMORA MACHEL')
    comment=forms.CharField(label='Add any Comments You Have', required=False, help_text='Coments Should Be 150 words ',
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
    # TimeReceived= forms.DateTimeField(label='Date You Receive The E36', required=True ,widget = forms.DateInput(
    #  attrs={
    #      'type':'date',
    #      'max':today_date ,
    #     'min':min_date
    #     }
    # ))

    class Meta: 
        model = Quotation
        fields = ['File','Name','Type','DateReceived','Receivedfrom','comments']
        
        
    