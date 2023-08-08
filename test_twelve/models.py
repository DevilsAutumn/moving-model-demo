from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UnrelatedModel(models.Model):
    old_name = models.CharField(max_length=100)
    price = models.IntegerField()
    

class Publisher(models.Model):
    name = models.CharField(max_length=200)

    books_published = models.ManyToManyField("test_thirteen.Book")


    def __str__(self):
        return self.name