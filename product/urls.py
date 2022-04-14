from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_all_products_view),

    path('<int:id>/edit/', views.edit_product_view),
    path('<int:id>/edit/success/', views.edit_success_view),

    path('add/', views.add_product_view),
    path('add/success/', views.add_product_success_view),
]