from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>/', views.car_pages, name='car_pages'),
    path('search/', views.search, name='search')
]