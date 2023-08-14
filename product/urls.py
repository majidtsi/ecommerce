from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('order/', views.order_pro, name='order_list'),
    path('', views.product_list,name='product'),
    path('category/<str:search>', views.product_search, name='product_search'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),


]