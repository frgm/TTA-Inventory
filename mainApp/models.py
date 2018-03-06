from django.db import models

class Employees(models.Model):
    ID_Emp = models.AutoField(primary_key=True)
    Role = models.IntegerField(default=0)

class Products(models.Model):
    ID_Prod = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Material = models.IntegerField(default=0)

class Locations(models.Model):
    ID_Loc = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Coordinates = models.CharField(max_length=200)
    
class Requisition(models.Model):
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateTimeField('')

class Requisition(models.Model):
    ID_Emp = models.ForeignKey(Employees, on_delete=models.CASCADE)
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateTimeField('')
    
class Stock(models.Model):
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    
class Distribution(models.Model):
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateTimeField('')