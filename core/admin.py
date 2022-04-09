from django.contrib import admin

from .models import GeeksModel


@admin.register(GeeksModel)
class GeeksModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


# admin.site.register(GeeksModel, GeeksModelAdmin)
