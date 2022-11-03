
from email.policy import default
from django.db import models

class Outpass_Details(models.Model):
    name=models.CharField(max_length=100)
    roomno=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    fromdate=models.CharField(max_length=100)
    fromtime=models.CharField(max_length=100)
    todate=models.CharField(max_length=100)
    totime=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    regno=models.CharField(max_length=100,default="")

class Complaint_Details(models.Model):
    name=models.CharField(max_length=100)
    roomno=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    complaint=models.CharField(max_length=100)
    resolution=models.CharField(max_length=100)
    regno=models.CharField(max_length=100,default="")

class Admin_Outpass_Details(models.Model):
    name=models.CharField(max_length=100)
    roomno=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    fromdate=models.CharField(max_length=100)
    fromtime=models.CharField(max_length=100)
    todate=models.CharField(max_length=100)
    totime=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    regno=models.CharField(max_length=100,default="")
   

class Admin_Complaint_Details(models.Model):
    name=models.CharField(max_length=100)
    roomno=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    complaint=models.CharField(max_length=100)
    resolution=models.CharField(max_length=100)
    regno=models.CharField(max_length=100,default="")

class Student_Details(models.Model):
    name=models.CharField(max_length=100)
    regno=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    