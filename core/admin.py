from django.contrib import admin

from .models import GeeksModel


class GeeksModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(GeeksModel, GeeksModelAdmin)
