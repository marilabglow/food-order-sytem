from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import (UserSerializer, RegisterSerializer, RestaurantSerializer,CartSerializer,
                          FoodCategorySerializer, FoodSerializer,OrderItemSerializer)
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from .models import Restaurant,Food,OrderItem,Food_deliver,FoodCategory,Cart
from django.db.models import Q,Sum,F

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
    """def get_queryset(self):
        queryset = Food.objects.filter(availability=True,read_only=True)
        return queryset"""
class Cart_view(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def perform_create(self, serializer):
            print(self.request.data)
            data = dict(self.request.data)
            print(data)
            food_id = data['food']
            print(food_id)
            quantity=data['quantity'][0]
            opj_get = Food.objects.get(id = int(food_id[0]))
            serializer.save(user = self.request.user,
                food = opj_get,
                price = opj_get.price,
                quantity = quantity)
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)      
class OrderItem_view(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    
    def perform_create(self, serializer):
        iterms = Cart.objects.filter(user=self.request.user.id)
        print(">>>>>>>>>>>>>>>>",iterms)
        total = iterms.aggregate(pro=Sum(F('price')*F('quantity')))['pro']
        print(total)
        tax = int(10)
        serializer.save(user_id= self.request.user.id,cart=iterms,total=total+ int(tax),tax=tax)
        
        
        







   


