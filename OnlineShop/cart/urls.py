from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('remove/<product_id>', views.CartRemove.as_view(), name='cart_remove'),
    path('add/<product_id>', views.CartAdd.as_view(), name='cart_add'),
    path('clear', views.CartClear.as_view(), name='cart_clear'),
    path('', views.CartDetail.as_view(), name='cart_detail'),

]