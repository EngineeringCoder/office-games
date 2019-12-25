from django.contrib import admin
from . import models

# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    fields = ('navn','kallenavn','registrert')

admin.site.register(models.Profil,ProfilAdmin)