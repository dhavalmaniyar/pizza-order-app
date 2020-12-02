from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import (PizzaView, PizzaEditRemoveView)

# router = routers.DefaultRouter()
# router.register(r'pizzaorder', views.PizzaViewSet)
# router.register(r'pizzaorder', views.PizzaViewSet)

urlpatterns = [
     path('', views.home, name='home'),
    # path('home', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('pizza/', PizzaView.as_view(), name='pizza-view'),
    path('pizza/<int:id>', PizzaEditRemoveView.as_view(), name='pizza-edit-remove-view'),
]
