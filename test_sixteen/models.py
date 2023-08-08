from django.db import models
from test_fifteen.models import TestFifteenModel

# Renamed TestSixteenModel to NewTestSixteenModel
class NewTestSixteenModel(models.Model):
    test_fourteen_model = models.ForeignKey("test_fifteen.TestFourteenModel", on_delete=models.CASCADE)
    test_fifteen_model = models.OneToOneField(TestFifteenModel, on_delete=models.CASCADE)
    some_data = models.CharField(max_length=50)

    def __str__(self):
        return f"TestSixteenModel - {self.some_data}"
