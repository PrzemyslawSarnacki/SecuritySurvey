from django.shortcuts import render, redirect
from .forms import ObjectDataForm, ObjectTypeForm, ServiceTypeForm, PrivateObjectForm, PublicObjectForm, TradeForm, BankingForm, OtherForm
from .models import ObjectData, ObjectType, ServiceType, ServiceObject
from django.views.decorators.csrf import csrf_protect


def home(request):
    if request.method == 'POST':
        return redirect('object_type')
    return render(request, 'Survey/home.html', {})

def object_data(request):
    form = ObjectDataForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('object_type')
    else:
        form = ObjectDataForm()
    return render(request, 'Survey/object_data.html', {'form': form})

def object_type(request):
    context = {}

    object_data = ObjectData.objects.last()
    if object_data == None:
        object_data = ObjectData.objects.create()
   
    service_object = ServiceObject.objects.last()
    if service_object == None:
        service_object = ServiceObject.objects.create(object_data=object_data)
   
    service_type = ServiceType.objects.last()
    if service_type == None:
        service_type = ServiceType.objects.create(service_object=service_object)

    object_type = ObjectType.objects.last()
    if object_type == None:
        object_type = ObjectType.objects.create(service_type=service_type)

    print('debug')

    if 'object_type' in request.POST.keys():
        print('debug1')
        object_type.object_type = request.POST['object_type']
        object_type.save()
        if request.POST['object_type'] == '0':
            print('debug11')
            service_type_form = ServiceTypeForm(request.POST, instance=service_type)
            if 'service_type' in request.POST.keys():
                if request.POST['service_type'] == '0':
                    print('debug111')
                    service_object_form = TradeForm(request.POST, instance=service_object)
                elif request.POST['service_type'] == '1':
                    print('debug112')
                    service_object_form = BankingForm(request.POST, instance=service_object)
                elif request.POST['service_type'] == '2':
                    print('debug113')
                    service_object_form = OtherForm(request.POST, instance=service_object)
                context['service_object_form'] = service_object_form
                if 'service_object' in request.POST.keys():
                    object_data_form = ObjectDataForm(request.POST, instance=object_data)
                    context['object_data_form'] = object_data_form
        elif request.POST['object_type'] == '1':
            service_type_form = PrivateObjectForm(request.POST, instance=service_type)
            print('debug12')
            if 'service_type' in request.POST.keys():
                object_data_form = ObjectDataForm(request.POST, instance=service_type)

        elif request.POST['object_type'] == '2':
            print('debug13')
            service_type_form = PublicObjectForm(request.POST, instance=service_type)
        context['service_type_form'] = service_type_form
    else:
        print('debug2')
        recipe = object_type.object_type
        print('debug3')
        if recipe == '0':
            print('debug4')
            service_type_form = ServiceTypeForm(request.POST, instance=service_type)
        elif recipe == '1':
            print('debug5')
            service_type_form = PrivateObjectForm(request.POST, instance=service_type)
        elif recipe == '2':
            print('debug6')
            service_type_form = PublicObjectForm(request.POST, instance=service_type)
            print('debug7')
        print('debug8')
        srv = service_type_form.save(commit=False)
 
    # context['object_data_form'] = object_data_form
    # context['service_object_form'] = service_object_form
    context['service_type_form'] = service_type_form
    context['object_type'] = ObjectTypeForm(request.POST or None)
    return render(request, 'Survey/object_type.html', context)

def service_object(request):
    form = ServiceTypeForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        service_type = form.cleaned_data.get('service_type')
        form.save()
        if request.POST['service_type'] == 'Trade':
            detail_form = TradeForm(request.POST)
        elif request.POST['service_type'] == 'Banking':
            detail_form = BankingForm(request.POST)
        elif request.POST['service_type'] == 'Other':
            detail_form = OtherForm(request.POST)
        context['detail_form'] = detail_form
    elif 'finish' in request.POST:
        return redirect('results')
    else:
        form = ServiceTypeForm()
    return render(request, 'Survey/service_type.html', context=context)

def private_object(request):
    form = PrivateObjectForm(request.POST)
    if form.is_valid():
        form.save()
        total_private_building_value = form.cleaned_data.get('total_private_building_value')
        return redirect('other_services')
    else:
        form = PrivateObjectForm()
    return render(request, 'Survey/private_object.html', {'form': form})

def public_object(request):
    form = PublicObjectForm(request.POST)
    if form.is_valid():
        form.save()
        visitors_per_hour = form.cleaned_data.get('visitors_per_hour')
        return redirect('other_services')
    else:
        form = PublicObjectForm()
    return render(request, 'Survey/public_object.html', {'form': form})

def results(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Survey/results.html', {})

