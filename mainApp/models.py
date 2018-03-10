from django.db import models

class Employees(models.Model):
    ID_Emp = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200) #Or phone number
    Password = models.CharField(max_length=200)
    Role = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ID_Emp

        
class Products(models.Model):
    ID_Prod = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Material = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ID_Prod

        
class Locations(models.Model):
    ID_Loc = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Latitude = models.IntegerField(default=0)
    Longitude = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ID_Loc

        
class Requisition(models.Model):
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateTimeField('')
    
    def __str__(self):
        return self.ID_Loc + self.ID_Prod + self.Quantity + self.Date


class Report(models.Model):
    ID_Emp = models.ForeignKey(Employees, on_delete=models.CASCADE)
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateTimeField('')
    
    def __str__(self):
        return self.ID_Loc + self.ID_Prod + self.ID_Emp + self.Quantity + self.Date
    
class Stock(models.Model):
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    
class Distribution(models.Model):
    ID_Loc = models.ForeignKey(Locations, on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateTimeField('')