from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class NewsArticle(models.Model):
    comment_m2m = models.ManyToManyField("test_eleven.comment")
    headline = models.CharField(max_length=200)
    content = models.TextField()

# class Comment(models.Model):
#     text = models.TextField()
#     m2m = models.ManyToManyField("test_eleven.mymodel")
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')

#     def __str__(self):
#         return f"Comment on {self.content_type} object"

