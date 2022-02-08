from django.urls import path
from .views import HomeView, CartView, ProductView, CheckoutView, login_view, cart_query_view

app_name = "frontend"

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("cart/", CartView.as_view(), name='cart'),
    path("product/", ProductView.as_view(), name='product'),
    path("checkout/", CheckoutView.as_view(), name='checkout'),
    path("login/", login_view, name="login"),
    path("cart-query/", cart_query_view, name="cart_query")

]
