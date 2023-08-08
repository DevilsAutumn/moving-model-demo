from django.db import models

# Create your models here.
class MainModel(models.Model):
    m2m_field = models.ManyToManyField('MyModelM2M')
    class Meta:
        db_table = "custom_db_table"



class MyModelM2M(models.Model):
    field_m2m = models.ManyToManyField('MainModel',through="test_seven.MyModel")
    field_fk = models.ForeignKey("test_seven.MyModel",on_delete=models.CASCADE)