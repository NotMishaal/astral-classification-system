from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Astral(models.Model): 
    #All are text inputs   
    astral_id = models.IntegerField(primary_key=True,default=None) 
    created_by = models.CharField(max_length=200,default=None)
    ultraviolet_filter = models.CharField(max_length=30)
    green_filter = models.CharField(max_length=30)
    near_infrared_filter = models.CharField(max_length=30)
    red_filter = models.CharField(max_length=30)
    infrared_filter = models.CharField(max_length=30)
    modified_julian_date = models.CharField(max_length=30)
    spectroscopic_objects_id = models.CharField(max_length=30)
    redshift_value = models.CharField(max_length=30)
    plate_id = models.CharField(max_length=30) 

