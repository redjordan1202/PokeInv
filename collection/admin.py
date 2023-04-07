from django.contrib import admin

# Register your models here.

from .models import CollectionItem, Collection

admin.site.register(CollectionItem)
admin.site.register(Collection)
