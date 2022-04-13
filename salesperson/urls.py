from django.urls import path

from . import views

urlpatterns = [
    path('', views.salesperson_all_staff_view),
    path('edit/', views.edit_salesperson_view),
    path('report/', views.salesperson_commision_report_view),
]