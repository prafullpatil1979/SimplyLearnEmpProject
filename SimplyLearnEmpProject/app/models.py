from django.db import models

# Create your models here.

class Company(models.Model):
    cName = models.CharField(primary_key='true',max_length=50,unique='true')
    cEmail = models.EmailField()
    cUrl = models.CharField(max_length=50)
    class Meta:
        db_table = "company"
    def __str__(self):
        return self.cName

class Employee(models.Model):
    eFname = models.CharField(primary_key='true',max_length=50,unique='true')
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"
    def __str__(self):
        return self.eFname
    
#class Login(models.Model):
#    UserName = models.CharField(max_length=50)
#    password = models.CharField(max_length=32)
#    class Meta:
#        db_table = "login"


