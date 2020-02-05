from django.db import models


class SecurityDegree(models.Model):
    degree_name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return f"Twój budynek posiada {self.degree_name} zabezpieczenia"

class Crimes(models.Model):
    crime_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'media/', max_length=255, null=True, blank=True)
    chart = models.ImageField(upload_to = 'media/', max_length=255, null=True, blank=True, default='media/wypadki_srednio.jpg')

    def __str__(self):
        return f"{self.description}"

class DistrictVisually(models.Model):
    district_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    crimes = models.ManyToManyField(Crimes)

    def __str__(self):
        return f"Twoja dzielnica to {self.district_name}"

class ObjectData(models.Model):
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
    STREET_TYPE = (
        ('0','Mała ulica, wioska'),
        ('1','Ulica średniej wielkości lub mało ruchliwe przedmieścia miasta'),
        ('2','Ulica lub ciąg komunikacyjny o dużym natężeniu ruchu'),
        )
    NEIGHBORING_BUILDINGS = (
        ('1','Brak lub daleko (ponad 100 m)'),
        ('2','Domy jednorodzinne'),
        ('3','Bloki mieszkalne'),
        ('4','Budynki usługowe'),
        ('5','Obiekty sportowe lub rozrywkowe'),
        )
    district = models.ForeignKey(DistrictVisually, on_delete=models.CASCADE, default=1)
    # district = models.CharField(max_length=255, choices=DISTRICTS)
    street_type = models.CharField(max_length=255, choices=STREET_TYPE)
    cctv = models.BooleanField(default=False)
    locals_night = models.BooleanField(default=False)
    neighboring_buildings = models.CharField(max_length=255, choices=NEIGHBORING_BUILDINGS)
    flammable_materials = models.BooleanField(default=False)


class ServiceObject(models.Model):
    OBJECT_PRIORITIES = (
        ('0', 'Obiekt NIEZALICZANY do infrastruktury krytycznej'),
        ('1', 'Obiekt ZALICZANY do infrastruktury krytycznej'),
    )
    VISITORS_PER_HOUR = (
        ('0', 'kilka do kilkunastu osób'),
        ('1', 'do 100 osób'),
        ('2', 'od 100 do 300'),
        ('3', 'powyżej 300'),
    ) 
    VALUES = (
        ('0', 'Wartość do 500 tys.'),
        ('1', 'Wartość  powyżej > 500 tys.'), 
        ('2', 'Wartość powyżej > 1 000 tys.'), 
        ('3', 'Wartość powyżej > 1 500 tys.'),
    )
    # Trade
    total_trading_building_value = models.CharField(max_length=200, choices=VALUES, null=True, blank=True)
    # Other
    total_service_building_value = models.CharField(max_length=200, choices=VALUES, null=True, blank=True)
    # Private
    total_private_building_value = models.CharField(max_length=200, choices=VALUES, null=True, blank=True)
    # Public 
    visitors_per_hour = models.CharField(max_length=200, choices=VISITORS_PER_HOUR, null=True, blank=True)
    object_priority = models.CharField(max_length=255, choices=OBJECT_PRIORITIES, null=True, blank=True)

    object_data = models.ForeignKey(ObjectData, on_delete=models.CASCADE)


class ObjectType(models.Model): 
    OBJECT_TYPE = (
             ('0','Obiekt handlowy'),
             ('1','Obiekt usługowy - prywatny'),
             ('2','Obiekt prywatny'),
             ('3','Obiekt publiczny'),
    )
    object_type = models.CharField(max_length=255, choices=OBJECT_TYPE, default='0')
    service_object = models.ForeignKey(ServiceObject, on_delete=models.CASCADE)
