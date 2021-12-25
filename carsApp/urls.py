from django.urls import path, include
from . import views
from rest_framework import routers
from carsApp import views

app_name = 'carsApp'

router = routers.SimpleRouter()
router.register("car-list", views.CarListViewSet)

router.register("cars/detail", views.DetailsViewset)

router.register("cars/order", views.OrderViewSet)

# router.register("cars/placed-orders",views.PlacedOrdersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
