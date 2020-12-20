from django.urls import path
from .views import customer_views, owner_views, registrations

urlpatterns = [
    path("",customer_views.listing,name="home"),
    path("show_cart",customer_views.show_cart,name="show_cart"),
    path("cart",customer_views.cart,name="cart"),
    path("place_order",customer_views.place_order,name="place_order"),

    path("register",registrations.register,name="register"),
    path("login",registrations.login,name="login"),
    path("logout",registrations.logout,name="logout"),

    path("add_plant",owner_views.add_plant,name="add_plant"),
    path("show_plant",owner_views.show_plant,name="show_plant"),
    path("show_order",owner_views.show_order,name="show_order"),   
]


