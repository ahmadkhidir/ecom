from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.auth import login, authenticate
from .models import Product, Category
from .forms import LoginForm
import json


class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        carousel = list(products)[-1:-4:-1]
        categories = Category.objects.all()
        login_form = LoginForm()

        context = {
            "carousel": carousel,
            "products": products,
            "categories": categories,
            "login_form": login_form
        }
        return render(request, "frontend/home.html", context)


def login_view(request):
    if request.method == 'POST':
        print(request.POST['username'])
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password
                            )
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "bad"})


def cart_query_view(request):
    if request.method == 'POST':
        data = request.POST
        query = data.get('q')
        p_id = data.get('p')

        if query == "empty_cart":
            user_cart = request.user.cart_set.last()
            print(user_cart.cartitem_set.count())
            if user_cart.cartitem_set.count() == 0:
                return JsonResponse({"status": True})
            else:
                return JsonResponse({"status": False})
        if p_id and query == "in_cart":
            user_cart = request.user.cart_set.last()
            cartitem = user_cart.cartitem_set.filter(product_id=p_id)
            if cartitem:
                cartitem.delete()
                return JsonResponse({"status": False})
            else:
                product = Product.objects.filter(id=p_id).first()
                if product:
                    user_cart.cartitem_set.create(product=product)
                    return JsonResponse({"status": True})
        return JsonResponse({"status": None})


class CartView(View):
    def get(self, request):
        return HttpResponse("cart")