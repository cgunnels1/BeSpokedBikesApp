from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('customers/', views.list_all_customers_view),
]
