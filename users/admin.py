from django.contrib.auth.admin import admin
from .models import Worker , Supplier , User

admin.site.register(Supplier)
admin.site.register(Worker)