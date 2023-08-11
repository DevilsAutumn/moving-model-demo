
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

# class Article(Post):
#     author = models.ForeignKey('test_twenty.Author', on_delete=models.CASCADE)
#     publication_date = models.DateTimeField()

#     def __str__(self):
#         return f"{self.title} by {self.author}"
