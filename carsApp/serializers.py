from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Car, CarVariation, Order, Paint, Wheel, Interior, AddOn


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'start_range', 'Time_to_60',
                  'top_speed', 'peak_power', 'base_price','img_url']


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarVariation
        fields = '__all__'


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = '__all__'

class OrderPaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = ['id']      


class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'

class OrderInteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = ['id']


class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheel
        fields = '__all__'

class OrderWheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheel
        fields = ['id']

class AddOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOn
        fields = '__all__'

class OrderAddOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOn
        fields = ['id']

class DetailsSerializer(serializers.ModelSerializer):
    paint = PaintSerializer(read_only=True, many=True)
    interior = InteriorSerializer(read_only=True, many=True)
    wheel = WheelSerializer(read_only=True, many=True)
    add_on = AddOnSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = '__all__'  # [paint, interior, wheel, add_on]


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'  

    





# from rest_framework import serializers
# from .models import Add_ons, Car_variation, Cars, Interior, Paint, Wheels

# class WheelsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model =Wheels
#         fields = '__all__'

   

# class PaintSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Paint
#         fields = '__all__'

# class InteriorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Interior
#         fields = '__all__'

# class Add_onsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Add_ons
#         fields = '__all__'

# class Car_variationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Car_variation
#         fields = '__all__'

# class CarsSeriliazer(serializers.ModelSerializer):

#     paint = PaintSerializer(read_only = True , many = True)
#     add_on = Add_onsSerializer(read_only = True , many = True)
#     wheel = WheelsSerializer(read_only = True , many = True)
#     interior = InteriorSerializer(read_only = True , many = True)
#     car_variation = Car_variationSerializer(read_only = True , many = True)
#     class Meta:
#         model = Cars
#         fields = ['id','model_name','car_image','peak_power','cargo_capacity','start_range','top_speed','weight','paint','interior','wheel','add_on','car_variation']





        