from django.contrib import admin

# Register your models here.
from assets import models


class NewAssetAdmin(admin.ModelAdmin):
    list_display = ['sn', 'model', 'manufacturer']
    list_filter = ['manufacturer', ]
    search_fields = ('sn',)


class AssetAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.User)
admin.site.register(models.Asset, AssetAdmin)
