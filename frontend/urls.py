from django.urls import path
from .views import HomeView, CartView, login_view, cart_query_view

app_name = "frontend"

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("cart/", CartView.as_view(), name='cart'),
    path("login/", login_view, name="login"),
    path("cart-query/", cart_query_view, name="cart_query")

]
