from django.shortcuts import render, redirect
from .forms import ObjectDataForm, ObjectTypeForm, PrivateObjectForm, PublicObjectForm, TradeForm, OtherForm
from .models import ObjectData, ObjectType, ServiceObject, SecurityDegree, DistrictVisually
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        object_data = ObjectData.objects.create()
        service_object = ServiceObject.objects.create(object_data=object_data)
        object_type = ObjectType.objects.create(service_object=service_object)
        return redirect('object_type')
    return render(request, 'Survey/home.html', {})


@login_required(login_url='/login/')
def object_data(request):
    object_data = ObjectData.objects.last()
    form = ObjectDataForm(request.POST, instance=object_data)
    if form.is_valid():
        form.save()
        return redirect('results')
    else:
        form = ObjectDataForm()
    return render(request, 'Survey/object_data.html', {'form': form})


@login_required(login_url='/login/')
def object_type(request):
    context = {}

    service_object = ServiceObject.objects.last()
    object_type = ObjectType.objects.last()
    context['object_type'] = object_type

    forms_dict = {
        "0": TradeForm,
        "1": OtherForm,
        "2": PrivateObjectForm,
        "3": PublicObjectForm,
    }

    if 'object_type' in request.POST.keys():
        object_type.object_type = request.POST['object_type']
        object_type.save()
        service_object_form = forms_dict[request.POST['object_type']](
            request.POST, instance=service_object)
    else:
        recipe = object_type.object_type
        service_object_form = forms_dict[recipe](
            request.POST, instance=service_object)
        if request.POST:
            service_object_form.save()
            return redirect('object_data')
        if service_object_form.is_valid():
            service_object_form.save()

    context['service_object_form'] = service_object_form
    context['object_type_form'] = ObjectTypeForm(request.POST or None)
    return render(request, 'Survey/object_type.html', context)


@login_required(login_url='/login/')
def results(request):
    context = {}
    service_object = ServiceObject.objects.last()
    object_type = ObjectType.objects.last()
    object_data = ObjectData.objects.last()
    context['object_data'] = object_data
    degree = categorize_building(object_type, service_object) 
    context['security_degree'] = SecurityDegree.objects.get(
        degree_name=f'{degree} Stopień zabezpieczenia obiektu prywatnego')
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Survey/results.html', context)


def categorize_building(object_type, service_object, object_data): 
    degree = 'I'
    # Trading
    if object_type.object_type == '0':
        degree = categorize_other(object_data.flammable_materials, service_object.total_trading_building_value)
    # Other
    elif object_type.object_type == '1':
        degree = categorize_other(object_data.flammable_materials, service_object.total_service_building_value)
    # Private
    elif object_type.object_type == '2':
        degree = categorize_private(service_object, object_data)
    # Public
    elif object_type.object_type == '3':
        degree = categorize_public(service_object)
    return degree


def categorize_other(flammable_materials, building_value):
    degree_dict = {
            True: {
                '0': 'III',
                '1': 'III',
                '2': 'III',
                '3': 'IV',
            },
            False: {
                '0': 'I',
                '1': 'II',
                '2': 'III',
                '3': 'IV',
            },
    }
    return degree_dict[flammable_materials][building_value]


def categorize_public(service_object):
    public_dict = {
            '0':{
                    '0': 'I',
                    '1': 'II',
                    '2': 'III',
                    '3': 'IV',
                },
            '1':{
                    '0': 'III',
                    '1': 'III',
                    '2': 'IV',
                    '3': 'IV',
                },
            }
    return public_dict[service_object.object_priority][service_object.visitors_per_hour]


def categorize_private(service_object, object_data):
    degree = "I"
    if object_data.street_type == '0' and object_data.locals_night == False:
        private_dict = {
                '0': 'I',
                '1': 'II',
                '2': 'III',
                '3': 'IV',
        }
        degree = private_dict[service_object.total_private_building_value]
    elif object_data.street_type == '2' and object_data.locals_night == False:
        private_dict = {
                '0': 'II',
                '1': 'III',
                '2': 'IV',
                '3': 'IV',
        }
        degree = private_dict[service_object.total_private_building_value]
    elif object_data.street_type == '1' or object_data.locals_night == True:
        private_dict = {
                '0': 'III',
                '1': 'III',
                '2': 'IV',
                '3': 'IV',
        }
        degree = private_dict[service_object.total_private_building_value]
    return degree
