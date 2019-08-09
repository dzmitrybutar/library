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
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('users_list')
        return render(request, 'users_list.html', {'form': form})


class DetailUserView(View):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        books = Book.objects.filter(user=user)
        context = {
            'user': user,
            'form': BookForm(),
            'books': books
        }
        return render(request, 'user_details.html', context=context)

    def post(self, request, pk):
        form = BookForm(request.POST)
        user = get_object_or_404(User, pk=pk)
        context = {
            'user': user,
            'form': form
        }
        if form.is_valid():
            film = form.save(commit=False)
            film.user = user
            film.save()
            return redirect('user_details', pk=pk)
        return render(request, 'user_details.html', context=context)


def book_edit(request, pk, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect('user_details', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_edit.html', {'form': form})

