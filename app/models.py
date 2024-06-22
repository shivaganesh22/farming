from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Production(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    acres=models.FloatField()
    facility=models.CharField(max_length=50)
    investment=models.FloatField()
    production=models.FloatField(blank=True,null=True)
    created=models.DateField(auto_now_add=True,blank=True,null=True)
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    price=models.FloatField()

class FarmingDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    farmer_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=12)
    contact_number = models.CharField(max_length=15)
    acres_ploughed = models.FloatField()
    season = models.CharField(max_length=50)
    crop_grown = models.CharField(max_length=100)
    seeds_used = models.CharField(max_length=50)
    date_seed_sown = models.DateField()
    transplanting = models.CharField(max_length=100)
    irrigation_method = models.CharField(max_length=100)
    fertilizers_used = models.CharField(max_length=100)
    date_harvesting = models.DateField()
    subfield = models.CharField(max_length=100)
    variety_used = models.CharField(max_length=100)
    quantity_used = models.CharField(max_length=50)
    irrigation_type = models.CharField(max_length=100)
    fertilizers_type = models.CharField(max_length=100)