from django.urls import path
from .views import (
    home,
    shop,
    cart,
    category_list,
    detail_page,
    go_register,
    add_to_cart, del_from_cart,
    del_from_cart
)


urlpatterns = [
    path('', home, name='index'),
    path('shop/', shop, name='shop'),
    path('goreg/', go_register, name='goreg'),
    path('detail/<int:pk>/', detail_page, name='detail'),
    path('cart/add/<int:product_id>/<int:user_id>/', add_to_cart, name='add_to_cart'),
    path('cart/del/<int:cart_item_id>/', del_from_cart, name='del_from_cart'),
    path('cart/', cart, name='cart'),
    path('shop/category/<slug:category_name>/', shop, name='shop_slug'),
    path('cart/add/<int:product_id>/', add_to_cart, name='cart_add'),
    path('categories/', category_list, name='category_list'),
    ]