from django.db import models
from django.core import validators
from .validators import validate_number

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone=models.CharField(max_length=10,null=True, validators=[validate_number])


    def __str__(self):
        return self.name
