from django.db import models
class Employee(models.Model):
   
    empcode=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
    salary=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)