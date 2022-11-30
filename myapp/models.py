from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

    
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    is_veg = models.BooleanField(default = True)
    address = models.TextField(max_length=50)
    ratings = models.IntegerField(help_text="enter 1 to 5")
    def __str__(self):
        return "{},{},{},{}".format(self.name, self.is_veg, self.address, self.ratings)
    
    
class FoodCategory(models.Model):
    food_cat= models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.food_cat)

class Food(models.Model):
    
    category = models.ForeignKey(FoodCategory, related_name="foods", on_delete=models.CASCADE,null=True)
    restaurant = models.ManyToManyField(Restaurant)
    food_name = models.CharField(max_length=50)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.category, self.restaurant, self.food_name,self.description,self.availability,self.price)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(Food, related_name="foods", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2,null = True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return "{},{},{},{}".format(self.user, self.food, self.quantity,self.food.price)
   
       

    
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    cart = models.ManyToManyField(Cart)
    tax = models.IntegerField(default = 18/100)
    total = models.DecimalField(max_digits=5, decimal_places=2,null = True)
   
    
class Food_deliver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    deliver_time = models.DateTimeField(auto_now_add=True)
    deliver_status = models.BooleanField(default = False)
     
    @property
    def food_deliver(self):
        deliver_time = timezone.now() + timezone.timedelta(days=1)
        return deliver_time
    
 


# Create your models here.
