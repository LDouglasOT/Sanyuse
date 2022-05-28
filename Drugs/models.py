from django.db import models

class Role(models.Model):
      Role_Name=models.CharField(max_length=100,blank=False,null=True)
      def __str__(self):
        return self.Role_Name


class Measurement(models.Model):
    Measurement=models.CharField(max_length=200,null=False,default="Tablets")
    def __str__(self):
        return self.Measurement

# Create your models here.
class Drug(models.Model):
    DrugName = models.CharField(max_length=200,null=False)
    Cost=models.IntegerField(null=False, blank=False)
    Profit=models.IntegerField(null=False, blank=False)
    Quantity=models.IntegerField(null=False, blank=False)
    Measured=models.ForeignKey(Measurement,on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return self.DrugName

    def checkProfit(self):
        TotalProfit=self.Profit*self.Quantity
        return TotalProfit;

    def get_full_cost(self):
        TotalCost=self.Quantity*self.Cost
        return TotalCost;

    def trackDrug(self,number):
        self.quantity -= number
    

class Employee(models.Model):
    Name=models.CharField(max_length=200,blank=False)
    Salary=models.CharField(max_length=200,null=False)
    PlaceOfResidence=models.CharField(max_length=200,null=False)
    Phone=models.CharField(max_length=200,null=False,blank=False)
    Phone1=models.CharField(max_length=200,null=True,blank=True)
    EmployMentDate=models.DateField(blank=False)
    Role=models.ForeignKey(Role,on_delete=models.CASCADE)
    ImageField=models.ImageField()
    Email=models.EmailField(max_length=200,null=False)
    CloseRelative=models.CharField(max_length=100,null=False)
    CloseRelativePhone1=models.CharField(max_length=100,null=False)
    CloseRelativePhone2=models.CharField(max_length=100,null=False)

    def __str__(self):
       return self.Name

class Expense(models.Model):
    Reason= models.CharField(max_length=200,blank=False)
    Amount=models.FloatField(max_length=200,blank=False)
    Date=models.DateField(auto_now_add=True,null=False)
    User=models.CharField(max_length=200,null=False,blank=True)
    def __str__(self):
        return self.Reason

class Patients(models.Model):
    Name=models.CharField(max_length=100,blank=False)
    Residence=models.CharField(max_length=100,null=False)
    Phone=models.CharField(max_length=100,null=False)
    PatientId=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.Name

class Treatment(models.Model):
    Treated=models.CharField(max_length=200,blank=False)
    PatientId=models.CharField(max_length=200,blank=False)
    def __str__(self):
        return self.Treated
    
class Balwadde(models.Model):
    Name=models.CharField(max_length=100,blank=False)
    Residence=models.CharField(max_length=100,null=False)
    Phone=models.CharField(max_length=100,null=False)
    PatientId=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.Name


class Appointment(models.Model):
    appointment=models.CharField(max_length=500,blank=False)
    Description=models.TextField(max_length=1000,blank=True)
    Date=models.DateField(blank=False,null=False)
    Person=models.ForeignKey(Employee, on_delete=models.CASCADE)






