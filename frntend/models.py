from django.db import models

class contactdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)
class registerdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    profile = models.ImageField(upload_to='profile', null=True, blank=True)

class booking_hoteldb(models.Model):
    peoples=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    hotel_name=models.CharField(max_length=100,null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)

class booking_placedb(models.Model):
    peoples=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)

class paymentdb(models.Model):
    cardnumber=models.IntegerField(null=True,blank=True)
    monthyear=models.DateField(null=True,blank=True)
    cvv=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)




class resrvationdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(max_length=100,null=True,blank=True)
    ch_out=models.DateField(max_length=100,null=True,blank=True)
    gust=models.CharField(max_length=100,null=True,blank=True)
    l_name=models.CharField(max_length=100,null=True,blank=True)
    mail=models.CharField(max_length=100,null=True,blank=True)
    ch_in=models.DateField(null=True,blank=True)
    types=models.CharField(max_length=100,blank=True,null=True)

class actdb(models.Model):
    activity=models.CharField(max_length=100,null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)




# Create your models here.
