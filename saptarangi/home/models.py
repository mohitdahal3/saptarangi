from django.db import models

# Create your models here.
class Available_product(models.Model):
   sno = models.AutoField(primary_key = True)
   name = models.CharField(max_length = 60)
   added_date = models.DateField()
   cost_price = models.IntegerField()
   marked_price = models.IntegerField()
   stock = models.IntegerField()
   buyed_party = models.CharField(max_length = 200)
   extra_information = models.TextField(default = '')

   def __str__(self):
      return self.name
   
   

class Sold_product(models.Model):
   sno = models.AutoField(primary_key = True)
   name = models.CharField(max_length = 60)
   added_date = models.DateField()
   sold_date = models.DateField()
   cost_price = models.IntegerField()
   marked_price = models.IntegerField()
   sold_price = models.IntegerField()
   buyed_party = models.CharField(max_length = 200)
   sold_party = models.CharField(max_length = 200)
   extra_information = models.TextField(default = '')

   def __str__(self):
      return self.name

