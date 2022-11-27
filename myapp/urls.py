from django.urls import path,include
from .views import *
from myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurant', views.Restaurantview,basename="restaurant")
router.register(r'food_cat', views.food_cat_view,basename="food cat")
router.register(r'food', views.food_view,basename="food")
router.register(r'cart', views.Cart_view,basename="CART")
router.register(r'orders', views.Order_view,basename="ORDER")
urlpatterns = [
  
  path("users",UserView.as_view()),
  path('register',RegisterView.as_view()),
  path('', include(router.urls)),

]

# Create a router and register our viewsets with it.

