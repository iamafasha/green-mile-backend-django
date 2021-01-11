from django.contrib.auth.admin import admin , UserAdmin
from .models import Worker , Supplier , User
from django.forms import ModelForm

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        exclude = []

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
admin.site.register(Supplier)
admin.site.register(Worker)