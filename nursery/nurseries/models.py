from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model) :
    customer =  models.OneToOneField(User,on_delete=models.CASCADE)

class Owner(models.Model) :
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    nursery_name = models.CharField(default="None",max_length=100, null=True)

class Plant(models.Model) :
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='plant_images', blank=True)
    name = models.CharField(default="None",max_length=100, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)

class Order(models.Model) :
    id = models.AutoField(primary_key=True)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE, null=True)
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True, null=True)
    delivered = models.BooleanField(null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    quantity = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
