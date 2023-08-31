from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Quotation(models.Model):
	name = [('VPN','VPN'),('Internet','Leased Line(Fibre)/Internet'),('VoIP','VoIP')]
	status = [('Completed','Completed'),('Pending','Pending')]
	File = models.FileField(_("E36"), upload_to='', max_length=100,null=True)
	NameClient = models.CharField(max_length=50,null=True,blank=True)	
	City = models.CharField(max_length=50,null=True,blank=True)	
	Total = models.DecimalField(_("Total"), max_digits=10, decimal_places=2,null=True)
	Status = models.CharField(_("Status of the E36"), max_length=50,choices=status,null = True)
	Type = models.CharField(max_length=50,null=True,blank=True,choices=name)
	#time and date of receiving the e36
	DateReceived=models.DateField(null=True, auto_now=False, auto_now_add=False)
	DateSubmited= models.DateField(null=True, auto_now=False, auto_now_add=False)
	TimeRecived = models.TimeField(_("Time Received"), auto_now=False, auto_now_add=False, null=True)
	TimeSubmitted = models.TimeField(_("TimeSubmited"), auto_now=False, auto_now_add=False ,null=True)
	created = models.DateTimeField(_("created at"), auto_now=True, auto_now_add=False ,null=True)
	updated = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
	#ends here
	Receivedfrom = models.CharField(_("Name of te Enginner WhomGive you The E36"),default='Enginner ' ,max_length=50)
	comments = models.TextField(_("Comments"),null =True,blank=True)
	WeekReport = models.IntegerField(_("Total amount of e36"),null=True)
	user = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE ,null=True)
	image = models.ImageField(upload_to = 'picture' ,null=True, blank = True)
 
 
	@property
	def ImageUrl(self):
		try:
		    url = self.image.url
		except:
		     url = ''
		     
		return url
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
  
	
