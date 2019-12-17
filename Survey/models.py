from django.db import models

class ObjectData(models.Model):
    SIZES = (
        ('parterowy','parterowy'),
        )
    DISTRICTS = (
        ('Bemowo','Bemowo'),
        )
    TRAFFIC_DAY = (
        ('1','0-5 aut/min'),
        )
    TRAFFIC_NIGHT = (
        ('1','0-1 aut/min'),
        )
    DISTANCE_FROM_THE_STREET = (
        ('1','<5 m'),
        )
    object_size = models.CharField(max_length=255, choices=SIZES)
    district = models.CharField(max_length=255, choices=DISTRICTS)
    traffic_day = models.CharField(max_length=255, choices=TRAFFIC_DAY)
    traffic_night = models.CharField(max_length=255, choices=TRAFFIC_NIGHT)
    distance_from_the_street = models.CharField(max_length=255, choices=DISTANCE_FROM_THE_STREET)
    cctv = models.BooleanField()
    locals_night = models.BooleanField()
    fence = models.CharField(max_length=255)
    landform = models.CharField(max_length=255)
    neighboring_buildings = models.CharField(max_length=255)

class ObjectType(models.Model): 
    object_type = models.CharField(max_length=255)

class ServiceObject(models.Model):
    SAFE_SIZES = (
        ('0','Mały sejf'),
        ('1','Duży sejf'),
        )
    # Trade
    total_products_value = models.DecimalField(decimal_places=2, max_digits=2)
    products_amount = models.IntegerField()
    # Banking
    safe_size = models.CharField(max_length=255, choices=SAFE_SIZES)
    # Other    
    total_service_building_value = models.DecimalField(decimal_places=2, max_digits=2)


class ServiceType(models.Model): 
    SERVICE_TYPES = (
        ('Trade','Usługi Handlowe'),
        ('Banking','Usługi Bankowe'),
        ('Other','Inne Usługi'),
        )
    service_type = models.CharField(max_length=255, choices=SERVICE_TYPES)
    service_object = models.ForeignKey(ServiceObject, on_delete=models.CASCADE)


class PrivateObject(models.Model):
    total_private_building_value = models.DecimalField(decimal_places=2, max_digits=2)


class PublicObject(models.Model):
    visitors_per_hour = models.IntegerField()
