from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Audio


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'id', 'uuid']


admin.site.register(CustomUser, CustomUserAdmin)


class AudioAdmin(admin.ModelAdmin):
    model = Audio
    list_display = ['id', 'file']


admin.site.register(Audio, AudioAdmin)
