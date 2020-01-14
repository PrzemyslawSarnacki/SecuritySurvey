from django.contrib import admin
from .models import ObjectData, ObjectType, ServiceObject

admin.site.register(ObjectData)
admin.site.register(ObjectType)
admin.site.register(ServiceObject)
