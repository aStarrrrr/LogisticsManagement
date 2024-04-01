from django.db import models
from Admin.models import *

class tbl_company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_contact = models.CharField(max_length=50)
    company_email = models.CharField(max_length=50)
    company_address = models.CharField(max_length=50)
    company_password = models.CharField(max_length=50)
    company_doj = models.DateField(auto_now_add=True)
    company_since = models.CharField(max_length=50)
    company_proof = models.FileField(upload_to='Files/')
    company_logo = models.FileField(upload_to='Files/')
    location_id = models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=50)
    owner_email = models.CharField(max_length=50)
    owner_contact = models.CharField(max_length=50)
    company_status = models.IntegerField(default=0)


class tbl_driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=50)
    driver_primary_contact = models.CharField(max_length=50)
    driver_secondary_contact = models.CharField(max_length=50)
    driver_email = models.CharField(max_length=50)
    driver_proof = models.FileField(upload_to='Files/')
    driver_photo = models.FileField(upload_to='Files/')
    driver_dob = models.CharField(max_length=50)
    driver_doj = models.DateField(auto_now_add=True)
    driver_password = models.CharField(max_length=50)
    driver_address = models.CharField(max_length=50)
    driver_expirence = models.CharField(max_length=50)
    location_id = models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    driver_status = models.IntegerField(default=0)
    
class tbl_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_contact = models.CharField(max_length=50)
    user_dob = models.CharField(max_length=50)
    user_doj = models.DateField(auto_now_add=True)
    user_address = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_aadhar_number = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_status = models.IntegerField(default=0)
    location_id = models.ForeignKey(tbl_location,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback_content = models.CharField(max_length=50)
    feedback_date = models.CharField(max_length=50)
    user_id = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    company_id = models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    driver_id = models.ForeignKey(tbl_driver,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint_content = models.CharField(max_length=50)
    complainttype_id = models.ForeignKey(tbl_complainttype,on_delete=models.CASCADE)
    complaint_date = models.CharField(max_length=50)
    complaint_status = models.IntegerField(default=0)
    complaint_reply = models.CharField(max_length=50, default='Not Yet Reply')
    user_id = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    company_id = models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    driver_id = models.ForeignKey(tbl_driver,on_delete=models.CASCADE)
    complaint_reply_date = models.CharField(max_length=50)