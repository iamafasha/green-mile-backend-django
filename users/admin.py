from django.contrib.auth.admin import UserAdmin , admin
from .models import Worker , Supplier , User


class WorkerAdmin(UserAdmin):
    pass

class SupplierAdmin(UserAdmin):
    pass

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Worker, WorkerAdmin)