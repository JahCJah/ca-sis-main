from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# class Student(models.Model):

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)  

class Account(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    class Meta:
        abstract=True # Don't use this line if you want Contact to have its own table

class Student(Account):
    student_firstname = models.CharField(max_length=128)
    student_lastname = models.CharField(max_length=128)
    student_grade_level = models.CharField(max_length=128, blank=True)
    status =[
    ('Not Enrolled','Not Enrolled'),
    ('Enrolled', 'Enrolled'),
    ]
    enrollment_status = models.CharField(max_length=20, choices=status,default='Not Enrolled')
    student_schoolyear_start=models.IntegerField(('year'), validators=[MinValueValidator(2000), max_value_current_year])

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class Teacher(Account):
    t_name = models.CharField(max_length=128)