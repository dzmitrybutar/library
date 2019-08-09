from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Book
from django.views import View
from .forms import BookForm, UserForm


class UserListView(View):

    def get(self, request):
        context = {
            'users': User.objects.all(),
            'form': UserForm()
        }
        return render(request, 'users_list.html', context=context)

    def post(self, request):
        context = {
            'users': User.objects.all(),
            'form': UserForm()
        }
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('users_list')
        return render(request, 'users_list.html', context=context)


def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    books = Book.objects.filter(user=user)
    return render(request, 'user_details.html', {'books': books, 'user': user})
