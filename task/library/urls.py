from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('user/<int:pk>/', views.user_details, name='user_detail_url'),
]