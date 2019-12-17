from django.shortcuts import render, redirect
from .forms import ObjectDataForm, ObjectTypeForm, ServiceTypeForm, PrivateObjectForm, PublicObjectForm, TradeForm, BankingForm, OtherForm
from django.views.decorators.csrf import csrf_protect


def home(request):
    if request.method == 'POST':
        return redirect('object_data')
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
    form = ObjectTypeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            object_type = form.cleaned_data.get('object_type')
            label = form.save(commit=False)
            if object_type == 'Obiekt usługowy':
                return redirect('service_object')
            elif object_type == 'Obiekt prywatny':
                return redirect('private_object')
            elif object_type == 'Obiekt publiczny':
                return redirect('public_object')
        else:
            form = ObjectTypeForm()
    return render(request, 'Survey/object_type.html', {'form': form})

def service_object(request):
    form = ServiceTypeForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        service_type = form.cleaned_data.get('service_type')
        form.save(commit=False)
        if request.POST['service_type'] == 'Trade':
            detail_form = TradeForm(request.POST)
        elif request.POST['service_type'] == 'Banking':
            detail_form = BankingForm(request.POST)
        elif request.POST['service_type'] == 'Other':
            detail_form = OtherForm(request.POST)
        context['detail_form'] = detail_form
    elif 'finish' in request.GET:
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

