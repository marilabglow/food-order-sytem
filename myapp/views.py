from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import (UserSerializer, RegisterSerializer, RestaurantSerializer,CartSerializer,
                          FoodCategorySerializer, FoodSerializer,OrderItemSerializer)
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from .models import Restaurant,Food,Cart,OrderItem,Food_deliver,FoodCategory


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]


class Restaurantview(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
class food_cat_view(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class =  FoodCategorySerializer
class food_view(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class =  FoodSerializer
class Cart_view(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =  CartSerializer
class Order_view(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class =  OrderItemSerializer
    

    

# Create your views here.
