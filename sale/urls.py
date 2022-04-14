from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_all_sales_view),
    path('create/', views.create_sale_view),
    path('create/success/', views.create_sale_success_view),
    path('report/', views.commision_report_view),
]