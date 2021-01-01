from django.db import models    
from django.conf import settings
from users.models import Supplier

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
    TYPE = (
        ('1', 'Envelope'),
        ('2', 'Parcel'),
        ('2', 'Soft'),
        ('2', 'Freezed'),
    )
    name = models.CharField(max_length=30)
    supplier = models.ForeignKey( Supplier , on_delete=models.DO_NOTHING)
    to =  models.ForeignKey(Shipping, default=None, on_delete=models.CASCADE )
    size = models.ForeignKey( PackageSize, default=None, on_delete=models.CASCADE )
    type = models.CharField(max_length=1, default="1", choices=TYPE)
    def __str__(self):
        return self.name