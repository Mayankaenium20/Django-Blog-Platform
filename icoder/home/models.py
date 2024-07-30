from django.db import models
from blog.models import Post

# Create your models here.
#models defined in django are same as that of sql tables as defined in the settings.py

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)            #this will uniquely identify this attribute and increment it automatically 
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True, blank = True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email