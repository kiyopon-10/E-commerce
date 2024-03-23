from django.urls import path
from .views import ProductListView, ProductDetailView, AddToCartView, UserCartItemsView

urlpatterns = [
    path("list/", ProductListView.as_view(), name='product-list'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product-detail'),
    path("add-to-cart/", AddToCartView.as_view(), name='add-to-cart'),
    path("user-cart-products/", UserCartItemsView.as_view(), name='user-cart-products'),
]