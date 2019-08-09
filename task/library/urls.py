from django.urls import path
from . import views
from .views import UserListView, DetailUserView

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('user/<int:pk>/', DetailUserView.as_view(), name='user_details'),
    path('user/<int:pk>/edit/<int:book_pk>/', views.book_edit, name='book_edit'),
]
