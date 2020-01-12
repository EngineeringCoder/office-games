from django.contrib import admin
from . import models
# Register your models here.


class MatchAdmin(admin.ModelAdmin):
    fields = ( models.Match.match_date)

admin.site.register(models.Match)
