from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    list_display = ("title","category","url")

admin.site.register(Page, PageAdmin)