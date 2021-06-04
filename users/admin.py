from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreation, UserChange

Custom = get_user_model()

class AdminRegistration(UserAdmin):
    form_class = UserCreation
    form = UserChange
    model = Custom

admin.site.register(Custom, AdminRegistration)