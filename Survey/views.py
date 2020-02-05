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

    # object_data = ObjectData.objects.last()
    service_object = ServiceObject.objects.last()
    object_type = ObjectType.objects.last()
    context['object_type'] = object_type

    if 'object_type' in request.POST.keys():
        object_type.object_type = request.POST['object_type']
        object_type.save()
        if request.POST['object_type'] == '0':
            service_object_form = TradeForm(
                request.POST, instance=service_object)
            # service_object_form.save()
        elif request.POST['object_type'] == '1':
            service_object_form = OtherForm(
                request.POST, instance=service_object)
        elif request.POST['object_type'] == '2':
            service_object_form = PrivateObjectForm(
                request.POST, instance=service_object)
        elif request.POST['object_type'] == '3':
            service_object_form = PublicObjectForm(
                request.POST, instance=service_object)
    else:
        recipe = object_type.object_type
        if recipe == '0':
            service_object_form = TradeForm(
                request.POST, instance=service_object)
            if request.POST:
                service_object_form.save()
                return redirect('object_data')
        elif recipe == '1':
            service_object_form = OtherForm(
                request.POST, instance=service_object)
            if request.POST:
                service_object_form.save()
                return redirect('object_data')
        elif recipe == '2':
            service_object_form = PrivateObjectForm(
                request.POST, instance=service_object)
            if request.POST:
                service_object_form.save()
                return redirect('object_data')
        elif recipe == '3':
            service_object_form = PublicObjectForm(
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
    # Trading
    if object_type.object_type == '0':
        if object_data.flammable_materials == True:
            if service_object.total_trading_building_value == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie handlowym')
            elif service_object.total_trading_building_value == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie handlowym')
            elif service_object.total_trading_building_value == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie handlowym')
            elif service_object.total_trading_building_value == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia w obiekcie handlowym')
        elif object_data.flammable_materials == False:
            if service_object.total_trading_building_value == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='I Stopień zabezpieczenia obiektu handlowego')
            elif service_object.total_trading_building_value == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='II Stopień zabezpieczenia obiektu handlowego')
            elif service_object.total_trading_building_value == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia obiektu handlowego')
            elif service_object.total_trading_building_value == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia obiektu handlowego')
    # Other
    elif object_type.object_type == '1':
        if object_data.flammable_materials == True:
            if service_object.total_service_building_value == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie usługowym')
            elif service_object.total_service_building_value == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie usługowym')
            elif service_object.total_service_building_value == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie usługowym')
            elif service_object.total_service_building_value == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia w obiekcie usługowym')
        elif object_data.flammable_materials == False:
            if service_object.total_service_building_value == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='I Stopień zabezpieczenia obiektu usługowego')
            elif service_object.total_service_building_value == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='II Stopień zabezpieczenia obiektu usługowego')
            elif service_object.total_service_building_value == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia obiektu usługowego')
            elif service_object.total_service_building_value == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia obiektu usługowego')

    # Private
    elif object_type.object_type == '2':
        if object_data.street_type == '0' and object_data.locals_night == False:
            if service_object.total_private_building_value == '0':
                # 1stopien
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='I Stopień zabezpieczenia obiektu prywatnego')
            elif service_object.total_private_building_value == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='II Stopień zabezpieczenia obiektu prywatnego')
                # 2
            elif service_object.total_private_building_value == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia obiektu prywatnego')
                # 3
            elif service_object.total_private_building_value == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia obiektu prywatnego')
                # 4
        elif object_data.street_type == '2' and object_data.locals_night == False:
            if service_object.total_private_building_value == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='II Stopień zabezpieczenia obiektu prywatnego')
            elif service_object.total_private_building_value == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie prywatnym')
            elif service_object.total_private_building_value == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia w obiekcie prywatnym')
            elif service_object.total_private_building_value == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia obiektu')
        elif object_data.street_type == '1' or object_data.locals_night == True:
            if service_object.total_private_building_value == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie prywatnym')
            elif service_object.total_private_building_value == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia obiektu')
            elif service_object.total_private_building_value == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia')
            elif service_object.total_private_building_value == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczeń')

    # Public
    elif object_type.object_type == '3':
        if service_object.object_priority == '0':
            if service_object.visitors_per_hour == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='I Stopień zabezpieczenia obiektu prywatnego')
            elif service_object.visitors_per_hour == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='II Stopień zabezpieczenia obiektu prywatnego')
            elif service_object.visitors_per_hour == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia obiektu prywatnego')
            elif service_object.visitors_per_hour == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia obiektu prywatnego')

        elif service_object.object_priority == '1':
            if service_object.visitors_per_hour == '0':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień zabezpieczenia w obiekcie publicznym')
            elif service_object.visitors_per_hour == '1':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='III Stopień w obiekcie publicznym')
            elif service_object.visitors_per_hour == '2':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień zabezpieczenia w obiekcie publicznym')
            elif service_object.visitors_per_hour == '3':
                context['security_degree'] = SecurityDegree.objects.get(
                    degree_name='IV Stopień w obiekcie publicznym')

    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Survey/results.html', context)

