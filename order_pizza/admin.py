from django.contrib import admin

# Register your models here.
from .models import Size,PizzaOrder,Topping
admin.register(Size,PizzaOrder,Topping)(admin.ModelAdmin)