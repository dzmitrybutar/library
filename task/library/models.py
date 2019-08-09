from django.db import models


class User(models.Model):
    user = models.CharField(max_length=20)

    def __str__(self):
        return self.user


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    pages = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.author} ({self.year})'
