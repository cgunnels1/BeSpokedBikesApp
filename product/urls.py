from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_all_products_view),
    path('edit/', views.edit_product_view),
]