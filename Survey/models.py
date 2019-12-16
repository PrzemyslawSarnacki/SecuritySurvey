from django.db import models

class ObjectData(models.Model):
    object_size = models.CharField()
    district = models.CharField()
    traffic_day = models.CharField()
    traffic_night = models.CharField()
    distance_from_the_street = models.CharField()
    cctv = models.BooleanField()
    locals_night = models.BooleanField()
    fence = models.CharField()
    landform = models.CharField()
    neighboring_buildings = models.CharField()

class ObjectType(models.Model): 
    service_building = models.BooleanField()
    
    trade_services = models.BooleanField()
    total_products_value = models.DecimalField()
    products_amount = models.IntegerField()
    
    banking_services = models.BooleanField() 
    large_safe = models.BooleanField()
    small_safe = models.BooleanField()
    
    other_services = models.BooleanField()
    total_service_building_value = models.DecimalField()

    private_building = models.BooleanField()
    total_private_building_value = models.DecimalField()

    public_building = models.BooleanField()
    visitors_per_hour = models.IntegerField()
