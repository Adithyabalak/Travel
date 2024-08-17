from django.db import models

class  destinationdb(models.Model):
    place=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    profile=models.ImageField(upload_to='profile',null=True,blank=True)


class packagedb(models.Model):
    country1=models.CharField(max_length=500,null=True,blank=True)
    place=models.CharField(max_length=500,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    days=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    profile3=models.ImageField(upload_to='profile',null=True,blank=True)
    profile1=models.ImageField(upload_to='profile',null=True,blank=True)
    profile2=models.ImageField(upload_to='profile',null=True,blank=True)

class hoteldb(models.Model):
    place=models.CharField(max_length=500,null=True,blank=True)
    profile=models.ImageField(upload_to='profile',null=True,blank=True)


class hotel_detailsdb(models.Model):
    place=models.CharField(max_length=500,null=True,blank=True)
    name=models.CharField(max_length=500,null=True,blank=True)
    description=models.CharField(max_length=500,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    profile1=models.ImageField(upload_to='profile',null=True,blank=True)
    profile2=models.ImageField(upload_to='profile',null=True,blank=True)
    profile3=models.ImageField(upload_to='profile',null=True,blank=True)
    profile4=models.ImageField(upload_to='profile',null=True,blank=True)
    profile5=models.ImageField(upload_to='profile',null=True,blank=True)


class activitidb(models.Model):
    activity=models.CharField(max_length=500,null=True,blank=True)
    hour=models.IntegerField(max_length=500,null=True,blank=True)
    price=models.IntegerField(max_length=500,null=True,blank=True)
    profile=models.ImageField(upload_to='profile',null=True,blank=True)


# Create your models here.
