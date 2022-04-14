from django.urls import path

from . import views

urlpatterns = [
    path('', views.salesperson_all_staff_view),
    path('<int:id>/edit/', views.edit_salesperson_view),
    path('<int:id>/edit/success/', views.edit_success_view),

    path('add/', views.add_salesperson_view),
    path('add/success/', views.add_salesperson_success_view),

]
