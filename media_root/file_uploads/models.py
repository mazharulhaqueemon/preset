from django.db import models
class student(models.Model):
    name =models.CharField(max_length=1000)
    description = models.CharField(max_length=100)
    image   = models.ImageField(upload_to='image/', blank=True, null=True)

    # class Meta:
    #     ordering=['-created']
    #
    def __str__(self):
         return self.name

# Create your models here.
