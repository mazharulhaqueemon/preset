import os
import uuid

from django.db import models

def post_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('post_image/', filename)
class Catagores(models.Model):
    catagories = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
         return self.catagories

class post(models.Model):
     title = models.CharField(max_length=200,blank=True,null=True)
     image = models.ImageField(upload_to=post_image, blank=True, null=True)
     fileupload = models.FileField(upload_to='file_uploads/', blank=True, null=True)
     premimum= models.BooleanField(default=False)
     catagories = models.ForeignKey(Catagores, on_delete=models.CASCADE, related_name='catagories_for_image', null=False,blank=False)

     def __str__(self):
         return self.title

