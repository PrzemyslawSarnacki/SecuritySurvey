from django.shortcuts import render, redirect
from .forms import ObjectDataForm, ObjectTypeForm, ServiceObjectForm, PrivateObjectForm, PublicObjectForm

def object_data(request):
    form = ObjectDataForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('object_type')
    else:
        form = ObjectDataForm()
    return render(request, 'object_data.html', {'form': form})

def object_type(request):
    form = ObjectTypeForm(request.POST)
    if form.is_valid():
        form.save()
        object_type = form.cleaned_data.get('object_type')
        if object_type == 'Obiekt usługowy':
            return redirect('service_object')
        elif object_type == 'Obiekt prywatny':
            return redirect('private_object')
        elif object_type == 'Obiekt publiczny':
            return redirect('public_object')
    else:
        form = ObjectTypeForm()
    return render(request, 'object_type.html', {'form': form})

def service_object(request):
    form = ServiceObjectForm(request.POST)
    if form.is_valid():
        form.save()
        service_type = form.cleaned_data.get('service_type')
        if service_type == 'Usługi handlowe':
            return redirect('trade_service')
        elif object_type == 'Usługi bankowe':
            return redirect('banking_service')
        elif object_type == 'Inne usługi':
            return redirect('other_services')
    else:
        form = ServiceObjectForm()
    return render(request, 'service_type.html', {'form': form})

def private_object(request):
    form = PrivateObjectForm(request.POST)
    if form.is_valid():
        form.save()
        total_private_building_value = form.cleaned_data.get('total_private_building_value')
        return redirect('other_services')
    else:
        form = PrivateObjectForm()
    return render(request, 'private_object.html', {'form': form})

def public_object(request):
    form = PublicObjectForm(request.POST)
    if form.is_valid():
        form.save()
        visitors_per_hour = form.cleaned_data.get('visitors_per_hour')
        return redirect('other_services')
    else:
        form = PublicObjectForm()
    return render(request, 'public_object.html', {'form': form})


