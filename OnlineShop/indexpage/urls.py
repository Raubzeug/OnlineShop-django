from django.urls import path
from . import views

app_name = 'indexpage' #SET THIS VARIABLE FOR EVERY APPLICATION!!!
urlpatterns = [
    path('', views.IndexPageView.as_view(), name = 'product_list'),
    path('<id>', views.ProductPageView.as_view(), name='product_page'),

]