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
    object_type = models.CharField()
    service_building = models.BooleanField()

class ServiceObject(models.Model):
    service_type = models.CharField()
    # Trade
    total_products_value = models.DecimalField()
    products_amount = models.IntegerField()
    # Banking
    large_safe = models.BooleanField()
    small_safe = models.BooleanField()
    # Other    
    total_service_building_value = models.DecimalField()


class PrivateObject(models.Model):
    total_private_building_value = models.DecimalField()


class PublicObject(models.Model):
    visitors_per_hour = models.IntegerField()
