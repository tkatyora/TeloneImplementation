from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Quotation(models.Model):
	name = [('VPN','VPN'),('Internet','Leased Line(Fibre)/Internet'),('VoIP','VoIP')]
	status = [('Completed','Completed'),('Pending','Pending')]
	File = models.FileField(_("E36"), upload_to='', max_length=100,null=True)
	NameClient = models.CharField(max_length=50,null=True,blank=True)	
	City = models.CharField(max_length=50,null=True,blank=True)	
	Total = models.DecimalField(_("Total"), max_digits=10, decimal_places=2,null=True,blank=True)
	Status = models.CharField( max_length=50,choices=status,null = True)
	Type = models.CharField(max_length=50,null=True,blank=True,choices=name)
	#time and date of receiving the e36
	DateReceived=models.DateField(null=True, auto_now=False, auto_now_add=False )
	DateSubmited= models.DateField(null=True, auto_now=False, auto_now_add=False,blank =True)
	TimeRecived = models.TimeField(_("Time Received"), auto_now=False, auto_now_add=False, null=True,blank=True)
	TimeSubmitted = models.TimeField(_("TimeSubmited"), auto_now=False, auto_now_add=False ,blank =True,null=True)
	created = models.DateTimeField(_("created at"), auto_now=True, auto_now_add=False ,null=True)
	updated = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
	#ends here
	Receivedfrom = models.CharField(_("Name of te Enginner WhomGive you The E36"),default='Enginner ' ,max_length=50)
	comments = models.TextField(_("Comments"),null =True,blank=True)
	WeekReport = models.IntegerField(_( "Weekly report"),default= 45,null=True)
	created_by = models.ForeignKey(User,  on_delete=models.CASCADE ,null=True,blank=True)
	image = models.ImageField(upload_to = 'picture' ,null=True, blank = True)
	survey = models.BooleanField(null = True ,default=False)
	
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
		# hours = (self.DateSubmited - self.DateReceived) * 7 
		# time = (self.TimeSubmitted.datetime.time() - self.TimeRecived.datetime.time())
		# duration = hours + time
		# striped_hours = str(duration).split('days',1)[0]
		
		start = str(self.TimeRecived)
		end = str(self.TimeSubmitted)
		start_time = datetime.strptime(start, '%H:%M:%S')
		end_time = datetime.strptime(end, '%H:%M:%S')
		duration = end_time - start_time
		duration_parts = str(duration).split(":")
		time_parts = duration_parts[:2]
		new_duration = ":".join(time_parts)
		# grater  = datetime.strptime('07:00', '%H:%M')
		# if start > grater:
		# 	start_time = datetime.strptime(new_duration, '%H:%M')
		# 	end_time = datetime.strptime('15:30', '%H:%M')
		# 	new_duration = end_time - start_time
		return str(new_duration)
         

    
    
 
	def __str__(self):
		return f'Advert for  { str(self.NameClient)}'
	class meta:
		ordering = ('-created',)
  
class Document(models.Model):
	File = models.FileField(_("Documents"), upload_to='', max_length=100,null=True)
	Name = models.CharField(max_length=50,null=True,blank=True)
	Created = models.DateTimeField(_("created at"), auto_now=True, auto_now_add=False ,null=True)
	Updated = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)	
	Created_by = models.OneToOneField(User, verbose_name=_("User Who Created The Document"), on_delete=models.CASCADE ,null=True)
	Discription = models.TextField(_("Discription"),null =True,blank=True)
	@property
	def FileUrl(self):
		try:
			url = self.File.url
		except:
				url = ''
				
		return url
	def __str__(self):
		return f'Document for  { str(self.Name)}'

class Contacts(models.Model):
	Name = models.CharField(max_length=50,null=True,blank=True)
	Created = models.DateTimeField(_("created at"), auto_now=True, auto_now_add=False ,null=True)
	Updated = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)	
	Created_by = models.OneToOneField(User, verbose_name=_("User Who Created The Document"), on_delete=models.CASCADE ,null=True)
	Extension = models.CharField(max_length=10,null =True,blank=True)

