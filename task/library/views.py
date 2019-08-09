from django.shortcuts import render, get_object_or_404
from .models import User, Book


def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    books = Book.objects.filter(user=user)
    return render(request, 'user_details.html', {'books': books, 'user': user})
