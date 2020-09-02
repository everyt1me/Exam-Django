from django import forms
from django.contrib import admin
from .models import Good

class GoodsAdminForm(admin.ModelAdmin):
    list_display = ("id", "name", "price", "color", "description", "image")
    list_display_links = ("id", "name", "description")
admin.site.register(Good, GoodsAdminForm)
