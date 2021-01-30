from django.db import models, connections
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class BookDetails(models.Model):
    ISNB = models.CharField(max_length = 100,primary_key = True)
    price = models.IntegerField() 
    noofcopies = models.IntegerField()
    title = models.CharField(max_length = 100)
    edition = models.CharField(max_length = 100) 
    author = models.CharField(max_length = 100)
    pbid = models.IntegerField()
    status = models.CharField(max_length = 100)
    catagery = models.CharField(max_length = 100)
    
    class Meta:
        db_table = "book"
class StaffDetails(models.Model):
    SSN = models.CharField(max_length = 255,primary_key = True)
    F_name = models.CharField(max_length = 255) 
    L_name = models.CharField(max_length = 255)
    Address = models.CharField(max_length = 255)
    salary = models.CharField(max_length = 255) 
    specified_task = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255, default='NULL') 
    class Meta:
        db_table = "staff_member"
class AdminDetails(models.Model):
    login_id = models.CharField(max_length = 255,primary_key = True)
    password = models.CharField(max_length = 255) 
    SSN = models.CharField(max_length = 255)
    class Meta:
        db_table = "administration"
class PubDetails(models.Model):
    ID = models.CharField(max_length = 255,primary_key = True)
    Name = models.CharField(max_length = 255) 
    pub_year = models.CharField(max_length = 255)
    class Meta:
        db_table = "publisher"
class UserDetails(models.Model):
    SSN = models.CharField(max_length = 100,primary_key = True)
    F_name = models.CharField(max_length = 100) 
    L_name = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    email_id = models.CharField(max_length = 100) 
    password = models.CharField(max_length = 100)
    catagery = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    class Meta:
        db_table = "user"


class LoanDetails(models.Model):
    SSN = models.CharField(max_length = 100,primary_key = True)
    ISNB = models.CharField(max_length = 100) 
    issue_date = models.CharField(max_length = 100)
    return_date = models.CharField(max_length = 100)
    fine = models.IntegerField() 
    class Meta:
        db_table = "lends_return"
class usersDetails(models.Model):
    SSN = models.CharField(max_length = 100,primary_key = True)
    F_name = models.CharField(max_length = 100) 
    L_name = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    email_id = models.CharField(max_length = 100) 
    password = models.CharField(max_length = 100)
    catagery = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
class booksDetails(models.Model):
    ISNB = models.CharField(max_length = 100,primary_key = True)
    price = models.IntegerField() 
    noofcopies = models.IntegerField()
    title = models.CharField(max_length = 100)
    edition = models.CharField(max_length = 100) 
    author = models.CharField(max_length = 100)
    pbid = models.IntegerField()
    status = models.CharField(max_length = 100)
    catagery = models.CharField(max_length = 100)
class loansDetails(models.Model):
    SSN = models.CharField(max_length = 100,primary_key = True)
    ISNB = models.CharField(max_length = 100) 
    issue_date = models.CharField(max_length = 100)
    return_date = models.CharField(max_length = 100)
    fine = models.IntegerField()    
class staffsDetails(models.Model):
    SSN = models.CharField(max_length = 100,primary_key = True)
    F_name = models.CharField(max_length = 100) 
    L_name = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    salary = models.CharField(max_length = 100) 
    specified_task = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100, default='NULL')
class pubsDetails(models.Model):
    ID = models.CharField(max_length = 255,primary_key = True)
    Name = models.CharField(max_length = 255) 
    pub_year = models.CharField(max_length = 255)  
