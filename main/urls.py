from django.urls import path
from main.views import home, car_detail

urlpatterns = [
    path('', home, name='home'),
    path('audi/', car_detail, {'brand': 'audi'}, name='audi'),
    path('mercedes/', car_detail, {'brand': 'mercedes'}, name='mercedes'),
    path('lada/', car_detail, {'brand': 'lada'}, name='lada'),
    path('haval/', car_detail, {'brand': 'haval'}, name='haval'),
]