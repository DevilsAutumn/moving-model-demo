from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)
    m2m_field=models.ManyToManyField("test_thirteen.book")

    def __str__(self):
        return self.name

class BookGenre(models.Model):
    book = models.OneToOneField("test_thirteen.Book", on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.book} - {', '.join(str(genre) for genre in self.genre.all())}"

# moved from test_twelve to test_thirteen
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("test_twelve.Author", on_delete=models.CASCADE)

    class Meta:
        db_table="test_twelve_book"

    def __str__(self):
        return self.title

