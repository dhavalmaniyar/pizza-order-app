from .models import PizzaOrder
from rest_framework.serializers import (ModelSerializer)

class PizzaSerializer(ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ('orderid','shape','size','top_type','amt')