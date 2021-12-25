from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.http import request
import datetime

# Create your models here.


class Paint(models.Model):
    colour = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.colour)


class Interior(models.Model):
    interior = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.interior)


class Wheel(models.Model):
    wheel = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.wheel)


class AddOn(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)
    description = models.TextField(null = True) 

    def __str__(self):
        return str(self.name)


class Car(models.Model):
    name = models.CharField(max_length=20, null=True)
    Time_to_60 = models.CharField(max_length=10, null=True)
    base_price = models.IntegerField(default=0, null=True)
    start_range = models.CharField(max_length=20, null=True)
    peak_power = models.CharField(max_length=20, null=True)
    top_speed = models.CharField(max_length=20, null=True)
    weight = models.CharField(max_length=20, null=True)
    cargo_capacity = models.CharField(max_length=20, null=True)
    power_train = models.CharField(max_length=20, null=True)
    acceleration = models.CharField(max_length=20, null=True)
    drag_coefficient = models.CharField(max_length=20, null=True)
    wheels = models.CharField(max_length=20, null=True)
    charging = models.CharField(max_length=20, null=True)
    img_url = models.CharField(max_length=200, null=True)
    paint = models.ManyToManyField(Paint)
    interior = models.ManyToManyField(Interior)
    wheel = models.ManyToManyField(Wheel)
    add_on = models.ManyToManyField(AddOn)

    def __str__(self):
        return str(self.name)


class CarVariation(models.Model):
    CHOICES = [
        ('plaid', 'plaid'),
        ('plaid+', 'plaid+'),
        ('long range', 'long range'),
    ]
    name = models.CharField(
        max_length=20,
        choices=CHOICES,
        default='plaid',
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    add_on_price = models.IntegerField(default=0)
    range = models.CharField(max_length=20)
    peak_power = models.CharField(max_length=20)
    top_speed = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    cargo_capacity = models.CharField(max_length=20)
    power_train = models.CharField(max_length=20)
    acceleration = models.CharField(max_length=20)
    drag_coefficient = models.CharField(max_length=20)
    wheels = models.CharField(max_length=20)
    charging = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    # name = models.CharField(max_length=20, null=True)
    # Time_to_60 = models.CharField(max_length=10, null=True)
    # base_price = models.IntegerField(default=0, null=True)
    # start_range = models.CharField(max_length=20, null=True)
    # peak_power = models.CharField(max_length=20, null=True)
    # top_speed = models.CharField(max_length=20, null=True)
    # weight = models.CharField(max_length=20, null=True)
    # cargo_capacity = models.CharField(max_length=20, null=True)
    # power_train = models.CharField(max_length=20, null=True)
    # acceleration = models.CharField(max_length=20, null=True)
    # drag_coefficient = models.CharField(max_length=20, null=True)
    # wheels = models.CharField(max_length=20, null=True)
    # charging = models.CharField(max_length=20, null=True)
    # img_url = models.CharField(max_length=200, null=True)
    paint = models.ForeignKey(Paint ,null = True, on_delete=models.CASCADE)
    interior = models.ForeignKey(Interior , null = True,on_delete=models.CASCADE)
    wheel = models.ForeignKey(Wheel,null = True,on_delete=models.CASCADE)
    add_on = models.ForeignKey(AddOn,null = True , on_delete=models.CASCADE)
    car = models.ForeignKey(Car,null = True , on_delete=models.CASCADE)
    car_variation = models.ForeignKey(CarVariation,null = True , on_delete=models.CASCADE)
    final_price = models.IntegerField(default =0)
    date = models.DateTimeField(default = datetime.datetime.now)

    def __str__(self):
        return str(self.car)




# from django.db import models

# # Create your models here.

# class Paint(models.Model):
#     color = models.CharField(max_length=20)   
#     price = models.IntegerField() 


# class Wheels(models.Model):
#     wheel = models.CharField(max_length=20) 
#     price = models.IntegerField() 

# class Interior(models.Model):
#     interior = models.CharField(max_length=20) 
#     price = models.IntegerField() 

# class Add_ons(models.Model):
#     name = models.CharField(max_length=10) 
#     price = models.IntegerField() 
#     description = models.TextField(null = True)
      
# class Cars(models.Model):
#     paint = models.ManyToManyField(Paint)
#     wheels = models.ManyToManyField(Wheels)
#     interior = models.ManyToManyField(Interior)
#     add_ons =  models.ManyToManyField(Add_ons)
#     car_image = models.ImageField(max_length=300 , null = True)
#     time_to_60 = models.IntegerField(null = True)
#     model_name = models.CharField(max_length=10,  null = True)
#     top_speed = models.IntegerField(null = True)
#     peak_power = models.IntegerField(null = True)
#     start_price = models.IntegerField(null = True)
#     charging = models.IntegerField(null = True)


#     def __str__(self):
#         return self.model_name

# class Car_variation(models.Model):
    
#     CHOICES = [
#         ('plaid', 'plaid'),
#         ('plaid+', 'plaid+'),
#         ('long range', 'long range'),
#     ]
#     variation_name = models.CharField(
#         max_length=20,
#         choices=CHOICES,
#         default='plaid',
#     )
#     car = models.ForeignKey(Cars , on_delete=models.CASCADE , null = True)
#     top_speed = models.IntegerField()
#     peak_power = models.IntegerField()
#     start_price = models.IntegerField()
#     start_range = models.IntegerField()
#     cargo_capacity = models.IntegerField()
#     weight = models.IntegerField()

#     def __str__(self):
#         return self.variation_name
        


 