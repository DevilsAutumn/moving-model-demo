from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)
    m2m_field=models.ManyToManyField("app_b.book")


class BookGenre(models.Model):
    book = models.OneToOneField("app_b.Book", on_delete=models.CASCADE)
    genre = models.ManyToManyField("app_b.Publisher")

#moved from app_a to app_b
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    books_published = models.ManyToManyField("app_b.Genre")

    class Meta:
        db_table="app_a_publisher"

#moved from app_a to app_b
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("app_a.Author", on_delete=models.CASCADE)

    class Meta:
        db_table="app_a_book"