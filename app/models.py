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

# class Location(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return 'Location is - {}'.format(self.name)

# class Stream(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return '{} is subject stream'.format(self.name)

# class College(models.Model):
#     name = models.CharField(max_length=100)
#     desc = models.TextField()

#     def __str__(self):
#         return  '{} ----- college name'.format(self.name)

# class University(models.Model):
#     name = models.CharField(max_length=100)
#     desc = models.TextField()

#     def __str__(self):
#         return  '{} ----- university name'.format(self.name)

# class AnotherData(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     university = models.ForeignKey(University, on_delete=models.CASCADE)

#     def __str__(self):
#         return '{} - loaction {} - stream {} - college {} - university '.format(self.location, self.stream, self.college, self.university)