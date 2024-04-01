from django.db import models
from Guest.models import *
from User.models import *
from Driver.models import *
from Admin.models import *

class tbl_company_driver(models.Model):
    company_driver_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    driver_id = models.ForeignKey(tbl_driver,on_delete=models.CASCADE)
    company_driver_status = models.IntegerField(default=0)
    company_driver_date = models.DateField(auto_now_add=True)


class tbl_driver_request(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_date = models.DateField(auto_now_add=True)
    request_status = models.CharField(max_length=10, default=0)
    company_id = models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    driver_id = models.ForeignKey(tbl_driver,on_delete=models.CASCADE)




class tbl_vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_chase_no = models.CharField(max_length=50)
    vehicle_reg_no = models.CharField(max_length=50)
    vehicle_insurance_date = models.CharField(max_length=50)
    vehicle_insurance_exp = models.CharField(max_length=50)
    vehicle_status = models.IntegerField(default=0)
    vehiclesubtype_id = models.ForeignKey(tbl_vehiclesubtype,on_delete=models.CASCADE)
    company_id = models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    vehicle_detailes = models.CharField(max_length=100)
    vehicle_name = models.CharField(max_length=50)
    vehicle_amount = models.CharField(max_length=50)
    vehicle_capacity = models.CharField(max_length=50)


class tbl_transport_shedule(models.Model):
    transport_shedule_id = models.AutoField(primary_key=True)
    transport_shedule_date = models.DateField(auto_now_add=True)
    transport_request_id = models.ForeignKey(tbl_transport_request,on_delete=models.CASCADE)
    transport_shedule_status = models.IntegerField(default=0)
    driver_1_id = models.ForeignKey(tbl_driver,on_delete=models.CASCADE,related_name="driver_1_id")
    driver_2_id = models.ForeignKey(tbl_driver,on_delete=models.CASCADE,related_name="driver_2_id")
    vehicle_id = models.ForeignKey(tbl_vehicle,on_delete=models.CASCADE)
