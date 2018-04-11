from django.db import models

class Employees(models.Model):
    ID_Emp = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, default='') #Or phone number
    Password = models.CharField(max_length=200, default='')
    Role = models.IntegerField(default='00000')
    ID_Loc = models.IntegerField(default=0) #not key, can repeat. Keep track of locations
    
    def __str__(self):
        return self.Name

        
class Products(models.Model):
    ID_Prod = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, default='')
    Material = models.FloatField(default=0)
    
    def __str__(self):
        return self.Name

        
class Locations(models.Model):
    ID_Loc = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=200, default='')
    Name = models.CharField(max_length=200, default='')
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    
    def __str__(self):
        return self.Name

        
class Requisition(models.Model):
    ID_Loc = models.ForeignKey('Locations', on_delete=models.CASCADE)
    #ID_Prod = models.ForeignKey('Products', on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateField('',primary_key=True)
    
    def __str__(self):
        return self.ID_Loc + self.ID_Prod + self.Quantity + self.Date.strftime('%d-/%m-/%Y')

class PredictedRequisition(models.Model):
    ID_Loc = models.ForeignKey('Locations', on_delete=models.CASCADE)
    #ID_Prod = models.ForeignKey('Products', on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateField('',primary_key=True)
    
    def __str__(self):
        return self.ID_Loc + self.ID_Prod + self.Quantity + self.Date.strftime('%d-/%m-/%Y')

class Report(models.Model): #stock of each item per day
    ID_Emp = models.ForeignKey('Employees', on_delete=models.CASCADE)
    ID_Loc = models.ForeignKey('Locations', on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey('Products', on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateField('')
    
    def __str__(self):
        return self.ID_Loc.ID_Loc + self.ID_Prod.ID_Prod + self.ID_Emp.ID_Emp + self.Quantity + self.Date.strftime('%d-/%m-/%Y')

        
class Restock(models.Model): #stock of each item needed
    ID_Loc = models.ForeignKey('Locations', on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey('Products', on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
        
    def __str__(self):
        return self.ID_Loc + self.ID_Prod + self.Quantity

        
class Distribution(models.Model): #currently unused
    ID_Loc = models.ForeignKey('Locations', on_delete=models.CASCADE)
    ID_Prod = models.ForeignKey('Products', on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Date = models.DateField('')
    
    def __str__(self):
        return self.ID_Loc + self.ID_Prod + self.Quantity + self.Date.strftime('%d-/%m-/%Y')      