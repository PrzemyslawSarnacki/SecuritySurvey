from django import forms

from .models import ObjectData, ServiceObject, ObjectType, DistrictVisually


class ObjectDataForm(forms.ModelForm):

    class Meta:
        model = ObjectData
        fields = (
            'district',
            'street_type',
            'flammable_materials',
            'cctv',
            'neighboring_buildings',
            'locals_night',
        )
        labels = {
            'district': 'Dzielnica',
            'street_type': 'Rodzaj ulic w okolicy i bezpośrednio przy obiekcie',
            'flammable_materials': 'Materiały łatwopalne w pobliżu?',
            'cctv': 'Czy monitoring uliczny obejmuje obiekt?',
            'neighboring_buildings': 'Sąsiednie budynki',
            'locals_night': 'Czy znajdują się lokale otwarte w nocy w sąsiadującej okolicy?',
        }


# class DistrictForm(forms.ModelForm):

#     class Meta:
#         model = Dis
#         fields = ('district_name', 'description', 'crimes')

class ObjectTypeForm(forms.ModelForm):

    class Meta:
        model = ObjectType
        fields = ('object_type',)
        labels = {'object_type': 'Typ obiektu', }


class TradeForm(forms.ModelForm):
    
    class Meta:
        model = ServiceObject
        fields = ('total_trading_building_value', )
        labels = {'total_trading_building_value': 'Całkowita szacowana wartość budynku (w tys. PLN)',}


class OtherForm(forms.ModelForm):
    class Meta:
        model = ServiceObject
        fields = ('total_service_building_value', )
        labels = {'total_service_building_value': 'Całkowita szacowana wartość budynku (w tys. PLN)',}


class PrivateObjectForm(forms.ModelForm):

    class Meta:
        model = ServiceObject
        fields = ('total_private_building_value',)
        labels = {'total_private_building_value': 'Całkowita szacowana wartość obiektu (w tys. PLN)', }


class PublicObjectForm(forms.ModelForm):

    class Meta:
        model = ServiceObject
        fields = ('visitors_per_hour', 'object_priority',)
        labels = {'total_products_value': 'Ilość odwiedzających na godzinę',
                'object_priority': 'Priorytet obiektu' 
                }
