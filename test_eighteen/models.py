from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)
    m2m_field=models.ManyToManyField("test_seventeen.book")

    def __str__(self):
        return self.name

# class BookGenre(models.Model):
#     book = models.OneToOneField("test_seventeen.Book", on_delete=models.CASCADE)
#     genre = models.ManyToManyField(Genre)
