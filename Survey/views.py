from django.shortcuts import render, redirect
from .forms import ObjectDataForm, ObjectTypeForm, PrivateObjectForm, PublicObjectForm, TradeForm, BankingForm, OtherForm
from .models import ObjectData, ObjectType, ServiceObject
from django.views.decorators.csrf import csrf_protect


def home(request):
    if request.method == 'POST':
        object_data = ObjectData.objects.create()
        service_object = ServiceObject.objects.create(object_data=object_data)
        object_type = ObjectType.objects.create(service_object=service_object)
        return redirect('object_type')
    return render(request, 'Survey/home.html', {})

def object_data(request):
    object_data = ObjectData.objects.last()
    form = ObjectDataForm(request.POST, instance=object_data)
    if form.is_valid():
        form.save()
        return redirect('results')
    else:
        form = ObjectDataForm()
    return render(request, 'Survey/object_data.html', {'form': form})

def object_type(request):
    context = {}

    # object_data = ObjectData.objects.last()
    service_object = ServiceObject.objects.last()
    object_type = ObjectType.objects.last()

    if 'object_type' in request.POST.keys():
        object_type.object_type = request.POST['object_type']
        object_type.save()
        if request.POST['object_type'] == '0':
            service_object_form = TradeForm(request.POST, instance=service_object)
            # service_object_form.save()
        elif request.POST['object_type'] == '1':
            service_object_form = BankingForm(request.POST, instance=service_object)
            print('bank')
        elif request.POST['object_type'] == '2':
            service_object_form = OtherForm(request.POST, instance=service_object)
        elif request.POST['object_type'] == '3':
            service_object_form = PrivateObjectForm(request.POST, instance=service_object)
        elif request.POST['object_type'] == '4':
            service_object_form = PublicObjectForm(request.POST, instance=service_object)
    else:
        recipe = object_type.object_type
        if recipe == '0':
            service_object_form = TradeForm(request.POST, instance=service_object)
            if request.POST:
                service_object_form.save()
                return redirect('object_data')
        elif recipe == '1':
            service_object_form = BankingForm(request.POST, instance=service_object)
            if request.POST:
                print('trade')
                service_object_form.save()
                return redirect('object_data')
        elif recipe == '2':
            service_object_form = OtherForm(request.POST, instance=service_object)
            if request.POST:
                service_object_form.save()
                return redirect('object_data')
        elif recipe == '3':
            service_object_form = PrivateObjectForm(request.POST, instance=service_object)
            if request.POST:
                service_object_form.save()
                return redirect('object_data')
        elif recipe == '4':
            service_object_form = PublicObjectForm(request.POST, instance=service_object)
            if request.POST:
                service_object_form.save()
                return redirect('object_data')
        service_object_form.save()
        
    context['service_object_form'] = service_object_form
    context['object_type_form'] = ObjectTypeForm(request.POST or None)
    return render(request, 'Survey/object_type.html', context)

def service_object(request):
    object_data = ObjectData.objects.last()
    print(object_data)
    service_object = ServiceObject.objects.create(object_data=object_data)
    print(service_object)
    
    service_type = ServiceType.objects.create(service_object=service_object)

    object_type = ObjectType.objects.create(service_type=service_type)


    
    form = ServiceTypeForm(request.POST, instance=service_type)
    context = {'form': form}
    if form.is_valid():
        service_type = form.cleaned_data.get('service_type')
        form.save()
        if 'service_type' in request.POST.keys():
            if request.POST['service_type'] == '0':
                detail_form = TradeForm(request.POST, instance=service_object)
            elif request.POST['service_type'] == '1':
                detail_form = BankingForm(request.POST, instance=service_object)
            elif request.POST['service_type'] == '2':
                detail_form = OtherForm(request.POST, instance=service_object)
            context['detail_form'] = detail_form
    elif 'finish' in request.POST:
        return redirect('results')
    else:
        print('warning')
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

