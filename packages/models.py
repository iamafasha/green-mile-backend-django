from django.db import models    
from django.conf import settings

class ShippingLocation(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()

class Shipping (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number =  models.CharField(max_length=14)
    email = models.EmailField()
    street_address = models.CharField(max_length=30)
    village = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    location = models.ForeignKey(ShippingLocation , default=None, on_delete=models.CASCADE )

    # Returns the string representation of the model.
    def __str__(self):
        return self.email

class PackageSize(models.Model):
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=30)
    supplier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    to =  models.ForeignKey(Shipping, default=None, on_delete=models.CASCADE )
    _type = (
        ('m', 'Hub Manager'),
        ('M', 'Officer'),
    )
    size = models.ForeignKey( PackageSize, default=None, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.name