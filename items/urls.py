from django.contrib import admin
from django.urls import path, include
from .views import Index, AddToCartView, MyCartView, ManageCartView, CheckoutView, confirm
from . import views


urlpatterns = [
    # path("login", views.login, name="login"),
    # path("", views.product, name="product"),
    path('search', views.search, name="search"),
    path('', Index.as_view(), name="home"), 
    path("add-to-cart<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my_cart", MyCartView.as_view(), name="my_cart"),
    path("manage_cart/<int:cp_id>/", ManageCartView.as_view(), name="manage_cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("confirm", views.confirm, name= "confirm"),
   # path("mycart", views.mycart, name="mycart"),
    # path("testing", views.testing, name="testing"),
    # path("logout", views.logout, name="logout"),
    # path("registration", views.registration, name="registration"),
]
