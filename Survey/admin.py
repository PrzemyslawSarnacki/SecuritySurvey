from django.contrib import admin
from .models import ObjectData, ObjectType, ServiceObject, SecurityDegree, Crimes, DistrictVisually

admin.site.register(ObjectData)
admin.site.register(ObjectType)
admin.site.register(ServiceObject)
admin.site.register(SecurityDegree)
admin.site.register(Crimes)
admin.site.register(DistrictVisually)
