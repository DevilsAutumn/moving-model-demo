from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.



class MyModel(models.Model):
    name = models.CharField(max_length=128)

# moved from test_ten to test_eleven
class Comment(models.Model):
    text = models.TextField()
    m2m = models.ManyToManyField("test_eleven.mymodel")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table="test_ten_comment"

    def __str__(self):
        return f"Comment on {self.content_type} object"