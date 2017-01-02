
from django.db import models
from django.contrib import admin
from django.db import models



 
# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    body =models.TextField()
    timestamp = models.DateTimeField()

    #def __str__(self):
        #return self.title
 
        

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


# Create your models here.
