from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, through='test_five.Membership')

