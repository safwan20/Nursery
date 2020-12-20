from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth
from ..models import Plant, Customer, Owner, Order
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from collections import defaultdict
import json
from .owner_views import *
from .registrations import *

def add_plant(request) :
    if request.user.is_authenticated :
        owner = Owner.objects.get(owner__username = request.user.username)
        if request.method == 'POST' :
            plant_name = request.POST.get('plant_name')
            price = request.POST.get('price')
            image = request.FILES['image']

            plant = Plant(owner=owner, image=image, name=plant_name, price=price)
            plant.save()

        params = {
            'owner' : owner
        }
        
        return render(request, "add_plant.html", params) 

    else :
        return HttpResponse("You are not a login user !!")


def show_plant(request) :
    if request.user.is_authenticated :
        owner = Owner.objects.get(owner__username = request.user.username)

        owner_plants = Plant.objects.filter(owner__owner = request.user)

        params = {
            'owner_plants' : owner_plants,
            'owner' : owner
        }

        return render(request, 'show_plant.html', params)
    
    else :
        return HttpResponse("You are not a login user !!")


def show_order(request) :
    if request.user.is_authenticated : 
        owner = Owner.objects.get(owner__username = request.user.username)

        orders = Order.objects.filter(plant__owner__owner__username=request.user.username)

        params  = {
            'orders' : orders,
            'owner' : owner
        }

        return render(request, "show_order.html", params) 
    else :
        return HttpResponse("You are not a login user !!")