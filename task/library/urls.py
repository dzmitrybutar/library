from django.urls import path
from . import views


urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('user/<int:pk>/', views.user_details, name='user_detail_url'),
]