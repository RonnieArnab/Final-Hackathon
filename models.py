from django.db import models

# Create your models here.

class footfall_DC(models.Model):
  footfall_data_dc=models.IntegerField(default=0)
  rec_dt_dc=models.DateTimeField()
  day_name_dc=models.CharField(max_length=200,default="NULL")

  def __str__(self):
    return self.day_name_dc

class footfall_FC(models.Model):
  footfall_data_fc=models.IntegerField(default=0)
  rec_dt_fc=models.DateTimeField()
  day_name_fc=models.CharField(max_length=200,default="NULL")

  def __str__(self):
    return self.day_name_fc

class footfall_library(models.Model):
  footfall_data_library=models.IntegerField(default=0)
  rec_dt_library=models.DateTimeField()
  day_name_library=models.CharField(max_length=200,default="NULL")

  def __str__(self):
    return self.day_name_library

class footfall_foodys(models.Model):
  footfall_data_foodys=models.IntegerField(default=0)
  rec_dt_foodys=models.DateTimeField()
  day_name_foodys=models.CharField(max_length=200,default="NULL")

  def __str__(self):
    return self.day_name_foodys

class footfall_bcourt(models.Model):
  footfall_data_bcourt=models.IntegerField(default=0)
  rec_dt_bcourt=models.DateTimeField()
  day_name_bcourt=models.CharField(max_length=200,default="NULL")

  def __str__(self):
    return self.day_name_bcourt 




