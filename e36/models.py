from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Quotation(models.Model):
	name = [('VPN','VPN'),('Internet','Leased Line(Fibre)/Internet'),('VoIP','VoIP')]
	status = [('Uncompleted','Uncompleted'),('Completed','Completed')]
	File = models.FileField(_("E36"), upload_to='', max_length=100)
	Name = models.CharField(max_length=50,null=True,blank=True)	
	Status = models.CharField(_("Status of the E36"), max_length=50,choices=status,null = True)
	Type = models.CharField(max_length=50,null=True,blank=True,choices=name)
	DateReceived=models.DateField(null=True, auto_now=False, auto_now_add=False)
	DateSubmited= models.DateField(null=True, auto_now=False, auto_now_add=True)
	Receivedfrom = models.CharField(_("Name of te Enginner WhomGive you The E36"),default='Enginner ' ,max_length=50)
	comments = models.TextField(_("Comments"),null =True,blank=True)
	#Duration = models.IntegerField(_("Time Taken To Sole The E36"),default=0)
	created = models.DateTimeField(_("created at"), auto_now=True, auto_now_add=False)
 
 
	@property
	def FileUrl(self):
		try:
			url = self.File.url
		except:
				url = ''
				
		return url
	@property
	def DurationField(self):
		hours = (self.DateSubmited - self.DateReceived) * 7 
		striped_hours = str(hours).split('days',1)[0]
		
		return striped_hours
         

    
    
 
	def __str__(self):
		return f'Advert for  { self.Name}'
	# class meta:
	# 	ordering = ('-created',)
  
	
