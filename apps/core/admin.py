from django.contrib import admin
from .models import *
from django.utils import timezone
from django.db.models import Sum


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'day_points')
    exclude = ('previous_day_points',)


admin.site.register(Profile, ProfileAdmin)