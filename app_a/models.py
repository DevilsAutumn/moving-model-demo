from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)


class UnrelatedModel(models.Model):
    old_name = models.CharField(max_length=100)
    price = models.IntegerField()

# class Publisher(models.Model):
#     name = models.CharField(max_length=200)
#     books_published = models.ManyToManyField("app_b.Genre")

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey("app_a.Author", on_delete=models.CASCADE)
