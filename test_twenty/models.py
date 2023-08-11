# models.py in the 'UserProfiles' app
from django.db import models
from test_nineteen.models import Post

class Author(models.Model):
    bio = models.TextField()

class Reader(models.Model):
    favorite_authors = models.ManyToManyField(Author, related_name='fans')
    article = models.ForeignKey("test_twenty.Article",on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey('test_nineteen.Post', on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    text = models.TextField()

# moved from test_nineteen to test_twenty
class Article(Post):
    author = models.ForeignKey('test_twenty.Author', on_delete=models.CASCADE)
    publication_date = models.DateTimeField()

    class Meta:
        db_table="test_nineteen_article"

    def __str__(self):
        return f"{self.title} by {self.author}"