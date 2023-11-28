from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from datetime import datetime, time, timedelta



# Create your models here.
class Quotation(models.Model):
	name = [('Internet','Internet'),('VPN','VPN')]
	status = [('Completed','Completed'),('Pending','Pending')]
	responsible = [('Dumisani_Mukuchura','Dumisani Mukuchura'),('Jervis_Tsoro','Jervis Tsoro'),('Shylet','Shylet'),('Godwin_Makara','Godwin Makara'),('MAaxwell_Mushaikwa','Maxwell Mushaikwa '),('Last_Sibasa','Last Sibasa')]
	File = models.FileField(_("E36"), upload_to='', max_length=100,null=True)
	NameClient = models.CharField(max_length=50,null=True,blank=True)	
	
	Total = models.DecimalField(_("Total"), max_digits=10, decimal_places=2,null=True,blank=True)
	Status = models.CharField( max_length=50,choices=status,null = True)
	Type = models.CharField(max_length=50,null=True,blank=True,choices=name)
	#time and date of receiving the e36
	DateReceived=models.DateField(null=True, auto_now=False, auto_now_add=False )
	DateSubmited= models.DateField(null=True, auto_now=False, auto_now_add=False,blank =True,default=timezone.now)
	TimeRecived = models.TimeField(_("Time Received"), auto_now=False, auto_now_add=False, null=True,blank=True)
	TimeSubmitted = models.TimeField(_("TimeSubmited"), auto_now=False, auto_now_add=False ,blank =True,null=True,default=timezone.now)
	created = models.DateTimeField(_("created at"), auto_now=True, auto_now_add=False ,null=True)
	updated = models.DateTimeField(null=True,auto_now=False,auto_now_add=True)
	#ends here
	Receivedfrom = models.CharField(_("Name of te Enginner WhomGive you The E36"),choices=responsible ,max_length=50,blank=True)
	comments = models.TextField(_("Comments"),null =True,blank=True)
	WeekReport = models.IntegerField(_( "Weekly report"),blank=True,null=True)
	created_by = models.ForeignKey(User,  on_delete=models.CASCADE ,null=True,blank=True)
	image = models.ImageField(upload_to = 'picture' ,null=True, blank = True)
	
	

	#METHODS TO CHANGE THE DATE FROM NOV. 23 2023 TO 23/11/23
	@property
	def startdate(self):
		if self.DateReceived is not None:
			return self.DateReceived.strftime("%d/%m/%Y")
		else:
			from datetime import date
			DateReceived = date(2023, 1, 1)
			return DateReceived.strftime("%d/%m/%Y")
	@property
	def enddate(self):
		if self.DateSubmited is not None:
			return self.DateSubmited.strftime("%d/%m/%Y")
		else:
			from datetime import date
			DateSubmited = date(2023, 1, 2)
			return DateSubmited.strftime("%d/%m/%Y")

	
	# PROPERTY FOR IMAGES

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
	
	# PROPERTIES TO CALCULATE THE DURATION
	@property
	def DurationField(self):
		# hours = (self.DateSubmited - self.DateReceived) * 7 
		# time = (self.TimeSubmitted.datetime.time() - self.TimeRecived.datetime.time())
		# duration = hours + time
		# striped_hours = str(duration).split('days',1)[0]
		number_days = 0
		start_date = self.DateReceived
		end_date = self.DateSubmited
		
		if start_date is not None and end_date is not None:
			days = end_date - start_date
			number_days = days.days - 1
		else:
			from datetime import date
			start_date = date(2023, 1, 1)
			end_date = date(2023, 1, 2)
			if start_date is None:
				print('Start date is Not provided')
			elif end_date is None:
				print('End date is none')
			days = end_date - start_date
			number_days = days.days - 1
		
		
	
		if days.days == 0:
			start = str(self.TimeRecived)
			end = str(self.TimeSubmitted)
			start_time = datetime.strptime(start, '%H:%M:%S')
			end_time = datetime.strptime(end, '%H:%M:%S')
			duration = end_time - start_time
			duration_parts = str(duration).split(":")
			time_parts = duration_parts[:2]
			new_duration = ":".join(time_parts)
		
		else:
			start = str(self.TimeRecived)
			end = str(self.TimeSubmitted)
			# Separating the Start time and end time since they are two diffrent days
			start_time_1 = datetime.strptime(start, '%H:%M:%S')
			end_time_1 = datetime.strptime('16:30:00', '%H:%M:%S')
			duration_1 = end_time_1 - start_time_1
			#getting second duration
			start_time_2 = datetime.strptime('08:00:00', '%H:%M:%S')
			end_time_2 = datetime.strptime(end, '%H:%M:%S')
			duration_2 = end_time_2 - start_time_2
			# Convert the time to a timedelta
			extra = datetime.strptime('00:00:00', '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')
			# Multiply the timedelta by 2
			extra *= number_days
			# Convert the timedelta back to a time
			extra = (datetime.min + extra)
			#Adding the time from days 
			duration = duration_1 + duration_2 + extra
			duration_parts = str(duration.time()).split(":")
			time_parts = duration_parts[:2]
			new_duration = ":".join(time_parts)		
		return str(new_duration)
	
	#METHOD TO CALCULAT THE TOTAL SURATION
	# @property
	# def total_duration(self):
	# 	total_duration = 0
	# 	for qoute in self.objects.all():
	# 		total_duration += qoute.DurationField
	# 	return total_duration

         

    
    
 
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

