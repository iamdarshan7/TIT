from django.db import models
from django.core import validators
from .validators import validate_number

# Create your models here.

class PercentageData(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class FacultyData(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone=models.CharField(max_length=10,null=True, validators=[validate_number])
    program = models.ForeignKey(FacultyData, on_delete=models.CASCADE)
    percentage = models.ForeignKey(PercentageData, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

