from django.db import models

class Post(models.Model):
    sno = models.AutoField(primary_key=True)            #this will uniquely identify this attribute and increment it automatically 
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length = 130)
    timestamp = models.DateTimeField(blank = True)

    def __str__(self):
        return self.title + ' by ' + self.author