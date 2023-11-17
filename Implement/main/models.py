from django.db import models
from django.utils.translation import gettext_lazy as _

class home(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to = 'picture' , blank = True)
    
    def __str__(self):
        return f'Advert for  { self.name}'
    
    
    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
             url = ''
             
        return url
class Contacts(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Created = models.DateTimeField(_("created at"), auto_now=True, auto_now_add=False ,null=True)
    Extension = models.CharField(max_length=10,null =True,blank=True)
    Department =models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f'Contact of  { self.Name}'
