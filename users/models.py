from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    login_count = models.PositiveIntegerField(default=0)
    
    @property
    def subclass(self):
        if hasattr(self, 'supplier'):
            return 'Supplier'
        elif hasattr(self, 'worker'):
            return 'Worker'
        return None

class Supplier(User):
    company_name= models.CharField(max_length=30)
    company_domain=models.CharField(max_length=30)
        
    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'
        
class Worker(User):
    ACCOUNT_TYPE = (
        ('1', 'Admin'),
        ('2', 'Regular'),
    )
    is_hub_manager = models.BooleanField(default=False)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE)
    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'