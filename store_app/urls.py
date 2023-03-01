from django.urls import path
from . import views

urlpatterns = [
    path('base/',views.BASE,name='base'),
    path('',views.HOME,name='home'),
    path('products/',views.PRODUCT,name='products'),
    path('products/<str:id>',views.PRODUCT_DETAIL_PAGE,name='product_detail'),
    path('contact/',views.Contact_Page,name='contact'),

    #path('auth/',views.AUTH,name='auth'),
    path('register/',views.HandleRegister,name='register'),
    path('login/',views.HandleLogin,name='login'),
    path('logout/',views.HandleLogout,name='logout'),
    #path('cart/cart_details/',views.CART,name='cart_details'),

    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout/',views.Check_out,name='checkout'),
    path('cart/checkout/placeorder/',views.PLACE_ORDER,name='place_order'),
    path('success/',views.success,name='success'),





    path('search/',views.SEARCH,name='search'),
    
]
