import django_filters
from .models import Size, PizzaOrder, Topping


class PizzaOrderFilter(django_filters.FilterSet):
    class Meta:
        model = PizzaOrder
        fields = '__all__'
