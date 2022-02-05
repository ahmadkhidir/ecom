from django.contrib import admin
from .models import Product, Image, Information, Category, Cart, CartItem

# Register your models here.
admin.site.register([Product, Image, Information, Category, Cart, CartItem])