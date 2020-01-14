from django.db import models

class ObjectData(models.Model):
    SIZES = (
        ('1','Parterowy'),
        ('2','Niski'),
        ('3','Średnio wysoki'),
        ('4','Wysokościowy'),
        )
    DISTRICTS = (
        ('1','Bemowo'),
        ('2','Białołęka'),
        ('3','Bielany'),
        ('4','Mokotów'),
        ('5','Ochota'),
        ('6','Praga Pd.'),
        ('7','Praga Pn.'),
        ('8','Rembertów'),
        ('9','Targówek'),
        ('10','Ursus'),
        ('11','Ursynów'),
        ('12','Wawer'),
        ('13','Wesoła'),
        ('14','Wilanów'),
        ('15','Włochy'),
        ('16','Wola'),
        ('17','Żoliborz'),
        )
    TRAFFIC_DAY = (
        ('1','0-5 aut/min'),
        ('2','5-10 aut/min'),
        ('3','10-50 aut/min'),
        ('4','50-100 aut/min'),
        ('5','100 < aut/min'),
        )
    TRAFFIC_NIGHT = (
        ('1','0-1 aut/min'),
        ('2','1-5 aut/min'),
        ('3','5-10 aut/min'),
        ('4','10-50 aut/min'),
        ('5','50 < aut/min'),
        )
    DISTANCE_FROM_THE_STREET = (
        ('1','<5 m'),
        ('2','5-10 m'),
        ('3','10 < m'),
        )
    FENCE = (
        ('1','Brak'),
        ('2','Niski płotek'),
        ('3','Płot o wysokości około 1,5 m'),
        ('4','Wysoki płot'),
        ('5','Płot 2-metrowy wraz z drutem kolczastym 0,5-metrowym'),
        )
    LANDFORM = (
        ('1','W zagłębieniu terenu do około 5m'),
        ('2','Równy teren'),
        ('3','Obok rzeki'),
        ('4','Na wzniesieniu terenu'),
        )
    NEIGHBORING_BUILDINGS = (
        ('1','Brak lub daleko (ponad 100 m)'),
        ('2','Domy jednorodzinne'),
        ('3','Bloki mieszkalne'),
        ('4','Budynki usługowe'),
        ('5','Obiekty sportowe lub rozrywkowe'),
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


class ServiceObject(models.Model):
    SAFE_SIZES = (
        ('0','Mały sejf'),
        ('1','Duży sejf'),
        )
    
    # Trade
    total_products_value = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    products_amount = models.IntegerField(null=True, blank=True)
    # Banking
    safe_size = models.CharField(max_length=255, choices=SAFE_SIZES, null=True, blank=True)
    # Other
    total_service_building_value = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    # Private
    total_private_building_value = models.DecimalField(decimal_places=2, max_digits=2, null=True, blank=True)
    # Public 
    visitors_per_hour = models.IntegerField(null=True, blank=True)

    object_data = models.ForeignKey(ObjectData, on_delete=models.CASCADE)


class ObjectType(models.Model): 
    OBJECT_TYPE = (
             ('0','Obiekt usług handlowych'),
             ('1','Obiekt usług bankowych'),
             ('2','Obiekt usług innych'),
             ('3','Obiekt prywatny'),
             ('4','Obiekt publiczny'),
    )
    object_type = models.CharField(max_length=255, choices=OBJECT_TYPE, default='0')
    service_object = models.ForeignKey(ServiceObject, on_delete=models.CASCADE)
