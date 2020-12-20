from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth
from ..models import Plant, Customer, Owner, Order
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from collections import defaultdict
import json
from .customer_views import *
from .registrations import *

carts = []

def listing(request) :
    if request.user.is_authenticated : 
        c = Customer.objects.filter(customer__username=request.user.username)
        o = Owner.objects.filter(owner__username=request.user.username)

        if len(c) != 0 :
            plant = Plant.objects.all()

            params = {
                'plants' : plant
            }
            
            return render(request,"listing.html", params)

        elif len(o) != 0 :
             return HttpResponse('Register as Customer !!!')
        
    else :
        return HttpResponse('You are not login !!!')


@csrf_exempt
def show_cart(request) :
    print("Show Cart !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    plant_data = json.loads(request.body)
    carts.append(plant_data['plant_data'])

    print(carts)
        
    return JsonResponse({
        'url' : '/cart'
    })

    
def cart(request) :
    cart_arr = defaultdict(list)

    for item in carts[0] :
        cart_arr[item].append(Plant.objects.get(id=item))
        cart_arr[item].append(carts[0][item])
        cart_arr[item] = tuple(cart_arr[item])

    params = {
        'carts_arr' : dict(cart_arr)
    }
    

    return render(request, "show_cart.html", params)


def place_order(request) :

    customer = Customer.objects.get(customer__username = request.user.username)

    for item in carts[0] :
        p = Plant.objects.get(id=item)


        order = Order(plant=p, quantity=carts[0][item], total=p.price, delivered=False, customer=customer)
        order.save()

        print(order.delivered, order.timestamp)

    return render(request, 'place_order.html')