from django.db import models

# Create your models here.

class Department(models.Model):

    class Meta:

        db_table = 'depart'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Employee(models.Model):

    class Meta:

        db_table = 'employee'

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name