from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    catname = models.CharField(max_length=100)
    catdes = models.CharField(max_length=300)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.catname

class PoliceStation(models.Model):
    policestationname = models.CharField(max_length=150)
    policestationcode = models.CharField(max_length=20)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.policestationname


class Police(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    policestationid = models.ForeignKey(PoliceStation, on_delete=models.CASCADE, null=True, blank=True)
    pid = models.CharField(max_length=20)
    address = models.CharField(max_length=200,null=True, blank=True)
    joiningdate = models.DateField()
    def __str__(self):
        return self.user.username


class Criminal(models.Model):
    criminalid = models.CharField(max_length=20)
    policeid = models.ForeignKey(Police, on_delete=models.CASCADE, null=True, blank=True)
    policestationid = models.ForeignKey(PoliceStation, on_delete=models.CASCADE, null=True, blank=True)
    catname = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    crimedate = models.DateField()
    crimetime = models.TimeField()
    prison = models.CharField(max_length=100)
    court = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contactno = models.CharField(max_length=15, null=True, blank=True)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    photo = models.FileField()
    recorddate = models.DateField()
    def __str__(self):
        return self.criminalid


class Fir(models.Model):
    firno = models.CharField(max_length=20, blank=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    policestationid = models.ForeignKey(PoliceStation, on_delete=models.CASCADE, null=True, blank=True)
    crimetype = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    nameaccused = models.CharField(max_length=150, blank=True)
    nameapplicants = models.CharField(max_length=150, blank=True)
    parentageapplicant = models.CharField(max_length=100, blank=True)
    contactno = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)
    relationaccused = models.CharField(max_length=100, null=True, blank=True)
    purposeoffir = models.CharField(max_length=200, blank=True)
    dateoffir = models.DateField(blank=True)
    remark = models.CharField(max_length=200,null=True, blank=True)
    status = models.CharField(max_length=20,null=True, blank=True)
    remarkdate = models.DateField(null=True, blank=True)
    sectionoflaw = models.CharField(max_length=150,null=True, blank=True)
    investigationofficer = models.CharField(max_length=100,null=True, blank=True)
    investigationdetail = models.CharField(max_length=300,null=True, blank=True)
    chargesheetdate = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.firno






