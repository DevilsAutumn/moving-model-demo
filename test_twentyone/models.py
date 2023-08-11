
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    book_m2m = models.ManyToManyField("test_twentytwo.book",related_name="book_m2m")

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        app_label = "test_twentytwo"
        db_table = "test_twentyone_book"
    
