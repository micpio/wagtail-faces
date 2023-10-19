from django.contrib import admin
from .models import Mybooksread
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    ordering = ['book_title',]
    list_display = ('book_title', 'authors', 'category')



admin.site.register(Mybooksread,PersonAdmin)
