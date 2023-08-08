from django.db import models

# Create your models here.
class SampleModel(models.Model):
    fk=models.ForeignKey("test_four.group",on_delete=models.CASCADE)
    m2m=models.ManyToManyField("test_four.person")

# moved from test_four to test_five
class Membership(models.Model):
    person = models.ForeignKey("test_four.person", on_delete=models.CASCADE)
    group = models.ForeignKey("test_four.group", on_delete=models.CASCADE)
    date_joined = models.DateField()
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = "test_four_membership"
    