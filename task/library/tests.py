from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Book, User
from django.urls import reverse


class LibTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_create(self):
        url = reverse('users_list')
        response = self.client.post(url, {'user': 'gvido'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(1, User.objects.count())

    def test_book_create(self):
        gvido = User.objects.create(user='gvido')
        self.assertEqual(1, User.objects.count())

        url = reverse('user_details', kwargs={'pk': gvido.pk})
        data = {
            'author': 'Author',
            'title': 'Book',
            'description': 'Description',
            'year': 2000,
            'pages': 100
            }
        response = self.client.post(url, data)
        book = Book.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(1, User.objects.count())
        self.assertEqual('Description', book.description)

    def test_edit_book(self):
        ben = User.objects.create(user='ben')
        self.assertEqual(ben, User.objects.get(id=ben.id))

        book = Book(
            author='Author',
            title='Book',
            description='Description',
            year=2000,
            pages=100,
            user=ben
        )
        book.save()
        self.assertEqual(1, Book.objects.all().count())
        book = Book.objects.first()
        url = reverse('book_edit', kwargs={
            'pk': ben.id,
            'book_pk': book.id,
        })
        new_data = {
            'author': 'Author2',
            'title': 'Book2',
            'description': 'Description',
            'year': 2000,
            'pages': 100
            }
        response = self.client.post(url, new_data)
        self.assertEqual(url, f'/user/{ben.id}/edit/{book.id}/')
        self.assertEqual(response.status_code, 302)
