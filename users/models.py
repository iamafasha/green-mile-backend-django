from django.db import models
from django.contrib.auth.models import AbstractUser

class AfashaUser(AbstractUser):
    login_count = models.PositiveIntegerField(default=0)

class Supplier(AfashaUser):
    company_name= models.CharField(max_length=30)
    company_domain=models.CharField(max_length=30)

class Worker(AfashaUser):
    account_type = [('', 'Envelope'), ('', 'Parcel') ]