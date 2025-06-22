from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),        # Главная страница
    path('new/', views.new),      # Страница /new/
    path('data/', views.data),    # Страница /data/
    path('test/', views.test)     # Страница /test/
]