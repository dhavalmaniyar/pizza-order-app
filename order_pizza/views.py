from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Size, Topping, PizzaOrder
from .filters import PizzaOrderFilter

# Create your views here.
from .serializers import PizzaSerializer


def home(request):
    pizzaBasePrice = 100
    allsize = Size.objects.all()
    alltop = Topping.objects.all()
    allorder = PizzaOrder.objects.all()
    myFilter = request.GET.get('topping')
    return render(request, 'home.html',
                  {'sizes': allsize, 'topping': alltop, 'orders': allorder, 'pizzaBasePrice': pizzaBasePrice,
                   'myFilter': myFilter})


class PizzaView(APIView):
    def get(self, request):
        shapeFilter = request.GET.get('shape')
        sizeFilter = request.GET.get('size')
        pizzaOrders = PizzaOrder.objects.all()

        if shapeFilter != None:
            pizzaOrders = pizzaOrders.filter(shape=shapeFilter.lower())

        if sizeFilter != None:
            pizzaOrders = pizzaOrders.filter(size=sizeFilter)

        serializer = PizzaSerializer(pizzaOrders, many=True)
        return Response({"response": serializer.data})

    def post(self, request):
        shape = request.data.get("shape")
        request.data["shape"] = shape.lower()
        if shape.casefold() != "regular" and shape.casefold() != "square":
            return Response(status=status.HTTP_400_BAD_REQUEST)


        size = request.data.get("size")
        isValidSize = Size.objects.filter(inches=size).exists()
        if not isValidSize:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PizzaEditRemoveView(APIView):
    def put(self, request, id):
        pizzaOrder = PizzaOrder.objects.get(id=id)
        serializer = PizzaSerializer(pizzaOrder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pizzaOrder = PizzaOrder.objects.get(id=id)
        pizzaOrder.delete()
        return Response(status=status.HTTP_200_OK)
