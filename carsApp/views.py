from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Car, CarVariation , Order
from .serializers import CarListSerializer, DetailsSerializer , OrderSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.


class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class DetailsViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = DetailsSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    

# class PlacedOrdersViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer






# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from . models import Cars
# from . serializers import CarsSeriliazer

# # Create your views here.
# class CarsList(APIView):
#     def get(self,request):
#         Car1 = Cars.objects.all()
#         serializer = CarsSeriliazer(Car1 , many = True)
#         return Response(serializer.data)

# class Car_detail(APIView):
#     def get(self,request,pk):
#         detail = Cars.objects.filter(id=pk)
#         serializer = CarsSeriliazer(detail , many =True)
#         return Response(serializer.data)

   

