from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from .models import Restaurant,Food,Cart,OrderItem,Food_deliver,FoodCategory



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "name","email"]


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  token = serializers.SerializerMethodField('get_user')

  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name','token')

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],  
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
  
  def get_user(self, obj):
    return Token.objects.get_or_create(user=obj)[0].key

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', "name","is_veg","address","ratings"]
class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['id', "food_cat"]
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', "food_name","category","restaurant","description",
                  "availability","price"]
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["food_name","quantity"]
class OrderItemSerializer(serializers.ModelSerializer):
    #total = serializers.SerializerMethodField('get_total')
    class Meta:
        model = OrderItem
        fields = ["order","shipping_address",]
        
  