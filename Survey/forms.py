from django import forms

class ObjectDataForm(forms.Form):
    object_size = forms.ChoiceField()
    district = forms.ChoiceField()
    traffic_day = forms.ChoiceField()
    traffic_night = forms.ChoiceField()
    distance_from_the_street = forms.ChoiceField()
    cctv = forms.BooleanField()
    locals_night = forms.BooleanField()
    fence = forms.ChoiceField()
    landform = forms.ChoiceField()
    neighboring_buildings = forms.ChoiceField()

class ObjectTypeForm(forms.Form):
    object_type = forms.ChoiceField()

class ServiceObjectForm(forms.Form):
    service_type = forms.ChoiceField()
    # Trade
    total_products_value = forms.DecimalField()
    products_amount = forms.IntegerField()
    # Banking
    large_safe = forms.BooleanField()
    small_safe = forms.BooleanField()
    # Other
    total_service_building_value = forms.DecimalField()


class PrivateObjectForm(forms.ModelForm):
    total_private_building_value = forms.DecimalField()


class PublicObjectForm(forms.ModelForm):
    visitors_per_hour = forms.IntegerField()
