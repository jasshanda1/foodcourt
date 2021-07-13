from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    

class Info(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    products = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Order(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    #fooditems = models.ForeignKey(Info,on_delete=models.CASCADE,default=0)
    selecteditems = models.IntegerField(max_length=100)
    totalamount = models.IntegerField(max_length=100)

# class Myorder(models.Model):
#     name = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
#     food_items = models.ForeignKey(Order,on_delete=models.CASCADE,default=0)
#     amount = models.ForeignKey(Order,on_delete=models.CASCADE,default=0)
    





