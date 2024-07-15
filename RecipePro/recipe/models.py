from django.db import models

# Create your models here.

class Receipe(models.Model):
    reciepe_name=models.CharField(max_length=100)
    reciepe_descr=models.TextField(max_length=100)
    reciepe_image=models.ImageField(upload_to="receipe")