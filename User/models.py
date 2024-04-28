from django.db import models
from Admin.models import *
from Guest.models import *
# from Company.models import *

class tbl_transport_request(models.Model):
    transport_request_id = models.AutoField(primary_key=True)
    transport_request_description = models.CharField(max_length=50)
    transport_request_date = models.DateField(auto_now_add=True)
    transport_request_qty = models.CharField(max_length=50)
    transport_request_rate = models.CharField(max_length=50,null=True)
    transport_request_for_date = models.CharField(max_length=50)
    transport_request_status = models.PositiveIntegerField(default=0)
    user_id = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    from_location_id = models.ForeignKey(tbl_location,on_delete=models.CASCADE,related_name="from_location_id")
    to_location_id = models.ForeignKey(tbl_location,on_delete=models.CASCADE,related_name="to_location_id")
    transport_request_reply = models.CharField(max_length=50, default='0')
    company_id = models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    category_id = models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    delivery_time = models.CharField(max_length=50)
    delivery_date = models.CharField(max_length=50)