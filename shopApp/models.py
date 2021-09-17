from django.db import models

# Create your models here.

class vegetables(models.Model):

    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='media')
    Quantity = models.IntegerField()
    Price = models.IntegerField()