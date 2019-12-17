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
    FENCE = (
        ('1','Brak'),
        )
    LANDFORM = (
        ('1','Równy teren'),
        )
    NEIGHBORING_BUILDINGS = (
        ('1','Bloki usługowe'),
        )
    object_size = models.CharField(max_length=255, choices=SIZES)
    district = models.CharField(max_length=255, choices=DISTRICTS)
    traffic_day = models.CharField(max_length=255, choices=TRAFFIC_DAY)
    traffic_night = models.CharField(max_length=255, choices=TRAFFIC_NIGHT)
    distance_from_the_street = models.CharField(max_length=255, choices=DISTANCE_FROM_THE_STREET)
    cctv = models.BooleanField(default=False)
    locals_night = models.BooleanField(default=False)
    fence = models.CharField(max_length=255, choices=FENCE)
    landform = models.CharField(max_length=255, choices=LANDFORM)
    neighboring_buildings = models.CharField(max_length=255, choices=NEIGHBORING_BUILDINGS)


class ObjectType(models.Model): 
    OBJECT_TYPE = (
             ('Obiekt usługowy','Obiekt usługowy'),
             ('Obiekt prywatny','Obiekt prywatny'),
             ('Obiekt publiczny','Obiekt publiczny'),
    )
    # object_type = models.CharField(max_length=255, choices=OBJECT_TYPE, null=True, blank=True)
    object_data = models.ForeignKey(ObjectData, on_delete=models.CASCADE)

class ServiceObject(models.Model):
    SAFE_SIZES = (
        ('0','Mały sejf'),
        ('1','Duży sejf'),
        )
    # Trade
    total_products_value = models.DecimalField(decimal_places=2, max_digits=10)
    products_amount = models.IntegerField()
    # Banking
    safe_size = models.CharField(max_length=255, choices=SAFE_SIZES, default=0)
    # Other    
    total_service_building_value = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)


class ServiceType(models.Model): 
    SERVICE_TYPES = (
        ('Trade','Usługi Handlowe'),
        ('Banking','Usługi Bankowe'),
        ('Other','Inne Usługi'),
        )
    service_type = models.CharField(max_length=255, choices=SERVICE_TYPES)
    service_object = models.ForeignKey(ServiceObject, on_delete=models.CASCADE)
    # object_type = models.ForeignKey(ObjectType, on_delete=models.CASCADE)


class PrivateObject(models.Model):
    # object_type = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
    total_private_building_value = models.DecimalField(decimal_places=2, max_digits=2)


class PublicObject(models.Model):
    # object_type = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
    visitors_per_hour = models.IntegerField()

