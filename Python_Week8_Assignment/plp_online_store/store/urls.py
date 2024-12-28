from django.urls import path
from .views import register, login_view, add_product, inventory, create_checkout_session, home, thank_you

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('add_product/', add_product, name='add_product'),
    path('inventory/', inventory, name='inventory'),
    path('create-checkout-session/<int:product_id>/', create_checkout_session, name='create_checkout_session'),
    path('thank_you/', thank_you, name='thank_you'),
]
