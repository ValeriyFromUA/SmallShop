from django.urls import path

from shop.views import ShopView, AboutView, ItemDetailView

urlpatterns = [
    path("shop/", ShopView.as_view(), name="shop"),
    path("items/<int:pk>", ItemDetailView.as_view(), name='item'),
    path("about/", AboutView.as_view(), name="about"),

]
