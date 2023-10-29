from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.car_index, name='car_index'),
    path('<int:pk>', views.car_detail, name='car_detail')
]