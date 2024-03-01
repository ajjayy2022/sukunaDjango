"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from.views import *

urlpatterns = [
    path ('',index),
    path ('login/', SignIn),
    path ('register/', register),
    path ('shop/',shop),
    path ('product/<int:id>', productDetails),
    path ('cart/', cart), 
    path ('logout/', user_logout),
    path ('add-to-cart/<int:product_id>', addToCart),
    path ('remove-from-cart/<int:cart_id>',removeFromCart),
    path ('checkout/', checkout),
    path ('myorder/', myorder),
    path ('add-to-wishlist/<int:product_id>', addtowishlist),
    path ('wishlist/', wishlist),
    path ('remove-from-wishlist/<int:wishlist_id>',removeFromWishlist)

]