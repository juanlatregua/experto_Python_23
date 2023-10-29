from django.urls import path
from review import views

urlpatterns = [
    path('', views.review_index, name='review_index'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
    path('<category>/', views.review_category, name='review_category')
]
