from django.db import models

# Create your models here.
class Bank(models.Model):
    name=models.CharField(max_length=200,blank=True)
    get_amount=models.IntegerField(blank=True)
    give_amount=models.IntegerField(blank=True)
    date_time=models.DateTimeField(auto_now_add=True)

class Telecom(models.Model):
    name=models.CharField(max_length=200,blank=True)
    get_amount=models.IntegerField(blank=True)
    give_amount=models.IntegerField(blank=True)
    date_time=models.DateTimeField(auto_now_add=True)

class Cement(models.Model):
    name=models.CharField(max_length=200,blank=True)
    get_amount=models.IntegerField(blank=True)
    give_amount=models.IntegerField(blank=True)
    date_time=models.DateTimeField(auto_now_add=True)

class Personal(models.Model):
    name=models.CharField(max_length=200,blank=True)
    get_amount=models.IntegerField(blank=True)
    give_amount=models.IntegerField(blank=True)
    date_time=models.DateTimeField(auto_now_add=True)
