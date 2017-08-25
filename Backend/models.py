from django.db import models

# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
    stud_class = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30, default='null')
