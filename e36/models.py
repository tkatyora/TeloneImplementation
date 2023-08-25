from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Quotation(models.Model):
	name = [('vpn','VPN'),('internet','Leased Line(Fibre)/Internet'),('VoIP','VoIP')]
	status = [('Uncompleted','Uncompleted'),('Completed','Completed')]
	File = models.FileField(_("E36"), upload_to=None, max_length=100)
	Name = models.CharField(max_length=50,null=True,blank=True)	
	Status = models.CharField(_("Status of the E36"), max_length=50,choices=status,null = True)
	Type = models.CharField(max_length=50,null=True,blank=True,choices=name)
	DateReceived=models.DateField(null=True, auto_now=False, auto_now_add=False)
	DateSubmited=models.DateField(null=True, auto_now=False, auto_now_add=True)
	Receivedfrom = models.CharField(_("Name of te Enginner WhomGive you The E36"),default='Enginner ' ,max_length=50)
	comments = models.TextField(_("Comments"))
	Duration = models.DurationField(_("Time Taken To Sole The E36"))
 
	def __str__(self):
		return f'Advert for  { self.Name}'

    
    
