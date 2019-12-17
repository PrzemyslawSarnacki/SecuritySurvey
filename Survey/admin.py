from django.contrib import admin
from .models import ObjectData, ObjectType, PrivateObject, PublicObject, ServiceObject, ServiceType

admin.site.register(ObjectData)
admin.site.register(ObjectType)
admin.site.register(PrivateObject)
admin.site.register(PublicObject)
admin.site.register(ServiceObject)
admin.site.register(ServiceType)
