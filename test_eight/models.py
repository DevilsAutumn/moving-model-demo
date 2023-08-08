from django.db import models

# class BaseModel(models.Model):
#     id=models.UUIDField(primary_key=True)

#     class Meta:
#         abstract=True

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    books_published = models.ManyToManyField("test_nine.Book")

    def __str__(self):
        return self.name

# class Book(BaseModel):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey("test_eight.Author", on_delete=models.CASCADE)


#     def __str__(self):
#         return self.title