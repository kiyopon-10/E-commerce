from django.urls import path
from .views import ProductListView, AddToCartView, UserCartItemsView

urlpatterns = [
    path("list/", ProductListView.as_view(), name='product-list'),
    path("add-to-cart/", AddToCartView.as_view(), name='add-to-cart'),
    path("user-cart-products/", UserCartItemsView.as_view(), name='user-cart-products'),
]