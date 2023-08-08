
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)

    books_published = models.ManyToManyField("test_seventeen.Book")


    def __str__(self):
        return self.name

# moved from test_eighteen to test_seventeen
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("test_seventeen.Author", on_delete=models.CASCADE)

    class Meta:
        managed=False
        db_table="test_eighteen_book"
    
    def __str__(self):
        return self.title