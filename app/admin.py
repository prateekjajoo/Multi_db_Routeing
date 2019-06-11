from django.contrib import admin
from .models import UserRole, Product
from .forms import UserRoleForm
from .views import UserCreateView
# Register your models here.


class UserRoleAdmin(admin.ModelAdmin):
    form = UserRoleForm
    view_on_site = UserCreateView


admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Product)
