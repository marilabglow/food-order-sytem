from django.contrib import admin
from .models import Restaurant,Food,Cart,OrderItem,Food_deliver,FoodCategory

admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Cart)
admin.site.register(Restaurant)
admin.site.register(OrderItem)
admin.site.register(Food_deliver)






# Register your models here.
