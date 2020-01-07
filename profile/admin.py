from django.contrib import admin
from . import models

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    fields = ('name','nickname','profile_text','trashtalk')
    list_display = ('name', 'nickname','joined')

admin.site.register(models.Profile,ProfileAdmin)