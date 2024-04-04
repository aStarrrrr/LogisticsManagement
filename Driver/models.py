from django.db import models
from Guest.models import *
from Company.models import tbl_transport_shedule


class tbl_driver_license(models.Model):
    driver_license_front_photo = models.FileField(upload_to='Files/')
    driver_license_back_photo = models.FileField(upload_to='Files/')
    driver_license_date = models.DateField(auto_now_add=True)
    driver_license_exp_date = models.CharField(max_length=50)
    driver_license_badge_exp_date = models.CharField(max_length=50)
    driver_license_class = models.CharField(max_length=50)
    driver_license_number = models.CharField(max_length=50)
    driver_license_id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(tbl_driver,on_delete=models.CASCADE)


class tbl_transport_update(models.Model):
    transport_shedule_id = models.ForeignKey(tbl_transport_shedule,on_delete=models.CASCADE)
    transport_update_id = models.AutoField(primary_key=True)
    transport_update_datetime = models.DateField(auto_now_add=True)
    transport_update_latitude = models.CharField(max_length=50)
    transport_update_longitude = models.CharField(max_length=50)
