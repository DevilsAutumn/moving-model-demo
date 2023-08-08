from django.db import models

# moved from test_one to test_two
class MyModel(models.Model):
    fkfk=models.ForeignKey("test_one.MyRelatedModels",on_delete=models.CASCADE)
    class Meta:
        db_table = "test_one_mymodel"

class MyOtherModel(models.Model):
    field_fk = models.ForeignKey("test_two.MyModel", on_delete=models.CASCADE,null=True)
