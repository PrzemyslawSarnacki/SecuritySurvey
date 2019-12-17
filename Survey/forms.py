from django import forms
from .models import ObjectData, ObjectType, PrivateObject, PublicObject, ServiceObject, ServiceType


class ObjectDataForm(forms.ModelForm):

    class Meta:
        model = ObjectData
        fields = (
            'object_size',
            'district',
            'traffic_day',
            'traffic_night',
            'distance_from_the_street',
            'cctv',
            'locals_night',
            'fence',
            'landform',
            'neighboring_buildings',
        )
        labels = {
            'object_size': 'Rozmiar',
            'district': 'Dzielnica',
            'traffic_day': 'Ruch w dzień',
            'traffic_night': 'Ruch w nocy',
            'distance_from_the_street': 'Odległość od ulicy',
            'cctv': 'Monitoring',
            'locals_night': 'Lokale otwarte w nocy w sąsiedztwie',
            'fence': 'Ogrodzenie',
            'landform': 'Ukształtowanie terenu',
            'neighboring_buildings': 'Sąsiednie budynki',
        }


class ObjectTypeForm(forms.ModelForm):

    class Meta:
        model = ObjectType
        fields = ('object_type',)
        labels = {'object_type': 'Typ obiektu', }


class BankingForm(forms.ModelForm):
    
    class Meta:
        model = ServiceObject
        fields = ('safe_size',)
        labels = {'safe_size': 'Rozmiar sejfu', }

class TradeForm(forms.ModelForm):
    
    class Meta:
        model = ServiceObject
        fields = ('total_products_value', 'products_amount')
        labels = {'total_products_value': 'Całkowita wartość produktów',
                'products_amount': 'Ilość produktów' 
                }


class OtherForm(forms.ModelForm):
    class Meta:
        model = ServiceObject
        fields = ('total_service_building_value', )
        labels = {'total_service_building_value': 'Całkowita wartość budynku',}

class ServiceTypeForm(forms.ModelForm):

    class Meta:
        model = ServiceType
        fields = ('service_type',)
        labels = {'service_type': 'Typ serwisu', }


class PrivateObjectForm(forms.ModelForm):

    class Meta:
        model = PrivateObject
        fields = ('total_private_building_value',)
        labels = {'total_private_building_value': 'Całkowita cena obiektu', }


class PublicObjectForm(forms.ModelForm):

    class Meta:
        model = PublicObject
        fields = ('visitors_per_hour',)
        labels = {'visitors_per_hour': 'Ilość odwiedzających na godzinę', }
