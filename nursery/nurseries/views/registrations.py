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
from .owner_views import *


def register(request) :
    if not request.user.is_authenticated : 
        if request.method == 'POST' :
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            types = request.POST.get('type') 

            password = make_password(password)

            print(email, username, password, types)

            if types == "owner" :
                nursery_name = request.POST.get('nursery_name')
                user = User(username=username, email=email, password=password)
                user.save()
                own = Owner(owner=user, nursery_name=nursery_name)
                own.save()
            else :
                user = User(username=username, email=email, password=password)
                user.save()
                cus = Customer(customer=user)
                cus.save()

            return redirect('/login')
    
        return render(request, "register.html")
    else :
        return HttpResponse("already login !!")


def login(request) :
    if not request.user.is_authenticated:
        if request.method == "POST" :
            username = request.POST.get('username')
            password = request.POST.get('password')  

            types = request.POST.get('type') 

            if types == 'customer' :
                c = Customer.objects.filter(customer__username=username)

                if len(c) != 0 :
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)

                    plant = Plant.objects.all()

                    params = {
                        'plants' : plant,
                        'customer' : c[0]
                    }

                    return render(request, "listing.html", params)
                
                else :
                    return HttpResponse('you are not customer')
            
            else :
                o = Owner.objects.filter(owner__username=username)

                if len(o) != 0 :
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)

                    param = {
                        'owner' : o[0]
                    }

                    return render(request, "owner.html", param)
                else :
                    return HttpResponse('you are not owner')
            
        else :
            return render(request, "login.html")

    else :
        c = Customer.objects.filter(customer__username=request.user.username)
        o = Owner.objects.filter(owner__username=request.user.username)
        
        if len(c) !=0 :
            plant = Plant.objects.all()
            
            params = {
                    'plants' : plant,
                    'customer' : c[0]
                }

            return render(request, "listing.html", params)

        elif len(o)!=0 :

            params = {
                'owner' : o[0]
            }

            return render(request, "owner.html", params)
            
        return render(request, "listing.html")



def logout(request) :
    if request.user.is_authenticated : 
        print(request.user)
        auth.logout(request)
        return HttpResponse("You have logout successfully !!")
    else :
        return HttpResponse("You are not a login user !!")
