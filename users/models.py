from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    login_count = models.PositiveIntegerField(default=0)
    
    @property
    def subclass(self):
        if hasattr(self, 'supplier'):
            return 'supplier'
        elif hasattr(self, 'worker'):
            return 'worker'
        return 'user'

class Supplier(User):
    company_name= models.CharField(max_length=30)
    company_domain=models.CharField(max_length=30)
    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'
        
class Worker(User):
    is_hub_manager = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'