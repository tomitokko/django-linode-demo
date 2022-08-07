from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    amount_of_teachers = models.IntegerField()
    amount_of_students = models.IntegerField()
    amount_of_subjects = models.IntegerField()
    owner = models.CharField(max_length=100)
    private = models.BooleanField()