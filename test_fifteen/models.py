from django.db import models

class TestFifteenModel(models.Model):
    test_fourteen_model = models.ForeignKey("test_fifteen.TestFourteenModel", on_delete=models.CASCADE,related_name="fourteen_model")
    f_m2m=models.ManyToManyField("test_fifteen.TestFourteenModel",through="test_sixteen.NewTestSixteenModel",related_name="fourteen_model_m2m")
    value = models.IntegerField()
    # Add your fields specific to the test_fifteen app here

    def __str__(self):
        return f"TestFifteenModel - {self.value}"

# moved from test_fourteen to test_fifteen
class TestFourteenModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table="test_fourteen_TestFourteenModel"
    def __str__(self):
        return self.name