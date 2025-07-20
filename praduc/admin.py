from django.contrib import admin
from .models import *
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['category','title','user']
    list_filter = ['category','user']
    search_fields = ['title__icontains']

admin.site.register(News, NewsAdmin)

admin.site.register(Category)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'user')
    search_fields = ('name', 'email', 'info')
    list_filter = ('created_at',)

admin.site.register(Contact, ContactAdmin)



admin.site.register(Comment)




