from django.contrib import admin

# Register your models here.
from .models import (Product, ShippingAddress, Order, OrderItem, Customer)


admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)