from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from .models import Manufacturer, Part
from django.db import models
from django.db.models.aggregates import Avg

# Create your views here.

def index(request):
    return render(request, 'index.html')

def me(request):
    return render(request, 'me.html')

def read_part(request):
    parts = Part.objects.all()
    return render(request, 'part/part_list.html',{"parts":parts})

def create_part(request):
    if request.method == 'GET':
        manufacturers = Manufacturer.objects.all()
        return render(request, 'part/create_part.html',{"manufacturers":manufacturers})
    else:
        data = {}
        for key in request.POST:
            if key in Part.__dict__:
                data[key] = request.POST[key]
        data['manufacturer'] = get_object_or_404(Manufacturer, pk=request.POST['manufacturer'])
        new_part = Part(**data)
        new_part.save()
        return redirect ('read_part')

def update_part(request, part_id):
    if request.method == 'GET':
        manufacturers = Manufacturer.objects.all()
        part = get_object_or_404(Part, pk=part_id)
        return render(request, 'part/update_part.html', {"part": part, "manufacturers": manufacturers})
    else:
        part = get_object_or_404(Part, pk=part_id)
        for key in request.POST:
            if key in part.__dict__ and key != 'manufacturer':
                setattr(part, key, request.POST[key])
        if 'manufacturer' in request.POST:
            setattr(part, 'manufacturer', get_object_or_404(
                Manufacturer, pk=request.POST['manufacturer']))
        part.save()
        return redirect('read_part')

def delete_part(request, part_id):
    part = get_object_or_404(Part, pk=part_id)
    part.delete()
    return redirect ('read_part')

def read_manufacturer(request):
    manufacturers = Manufacturer.objects.all()
    print(Manufacturer.objects.all())
    return render(request, 'manufacturer/manufacturer_list.html', {"manufacturers": manufacturers})


def create_manufacturer(request):
    if request.method == 'GET':
        return render(request, 'manufacturer/create_manufacturer.html')
    else:
        new_manufacturer = Manufacturer(name=request.POST['name'])
        new_manufacturer.save()
        return redirect('read_manufacturer')


def update_manufacturer(request, manufacturer_id):
    if request.method == 'GET':
        manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
        return render(request, 'manufacturer/update_manufacturer.html', {"manufacturer": manufacturer})
    else:
        manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
        for key in request.POST:
            if key in manufacturer.__dict__:
                setattr(manufacturer, key, request.POST[key])
        manufacturer.save()
        return redirect('read_manufacturer')


def delete_manufacturer(request, manufacturer_id):
    manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    manufacturer.delete()
    return redirect('read_manufacturer')

def report(request):
    expensive_parts = Part.objects.filter(cost__gt=1000)
    avg_prices = []
    for manufacturer in Manufacturer.objects.all():
        avg_prices.append({"manufacturer": manufacturer,  "price": Part.objects.filter(
            manufacturer=manufacturer.pk).aggregate(Avg('cost'))['cost__avg']})
    return render(request, 'report.html', {"expensive_parts": expensive_parts, "avg_prices": avg_prices})