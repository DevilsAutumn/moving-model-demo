from django.db import models

# Create your models here.
# class MyModel(models.Model):
#     fkfk=models.ForeignKey("test_one.MyRelatedModels",on_delete=models.CASCADE)

class MyRelatedModels(models.Model):
    field_fk = models.ForeignKey("test_two.MyModel", models.CASCADE)
    field_m2m = models.ManyToManyField("test_two.MyModel", related_name="many")
