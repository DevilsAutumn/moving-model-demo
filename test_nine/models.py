from django.db import models


class BaseModel(models.Model):
    id=models.UUIDField(primary_key=True)

    class Meta:
        abstract=True

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BookGenre(models.Model):
    book = models.OneToOneField("test_nine.Book", on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.book} - {', '.join(str(genre) for genre in self.genre.all())}"

# moved from test_eight to test_nine
class Book(BaseModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("test_eight.Author", on_delete=models.CASCADE)

    class Meta:
        db_table ="test_eight_book"

    def __str__(self):
        return self.title