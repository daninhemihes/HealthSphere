from django.db import models

# Create your models here.
class tbUser(models.Model):
    username = models.CharField(max_length=24, unique=True, null=False)
    email = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)

class tbPerson(models.Model):
    username = models.ForeignKey('TbUser', on_delete=models.PROTECT)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=25)
    sex = models.CharField(max_length=1)
    birthDate = models.DateField
    bloodType = models.CharField(max_length=3)
    organDonor = models.BooleanField
    weight = models.FloatField
    height = models.FloatField
    maritalStatus = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    nationality = models.CharField(max_length=25)
    occupation = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    phone = models.CharField(max_length=11)
    primaryLanguague = models.CharField(max_length=25)

class tbEmergencyContact(models.Model):
    username = models.ForeignKey('TbUser', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)

class tbMedicalConditions(models.Model):
    username = models.ForeignKey('TbUser', on_delete=models.PROTECT)
    medicalCondition = models.CharField(max_length=50)
    note = models.TextField(max_length=1000)

class tbAllergiesReactions(models.Model):
    username = models.ForeignKey('TbUser', on_delete=models.PROTECT)
    allergiesReactions = models.CharField(max_length=50)
    notes = models.TextField(max_length=1000)