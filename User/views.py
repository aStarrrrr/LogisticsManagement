from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Company.models import *
from Guest.models import *

def HomePage(request):
    return render(request,"User/HomePage.html")

def SearchCompany(request):
    state = tbl_state.objects.all()
    return render(request,"User/SearchCompany.html",{'state':state})

def SendRequest(request,cid):
    category = tbl_category.objects.all()
    state = tbl_state.objects.all()
    if request.method == "POST":
        selectedCategory = tbl_category.objects.get(category_id=request.POST.get("sel_category"))
        selectedFromLocation = tbl_location.objects.get(location_id=request.POST.get("sel_from_location"))
        selectedToLocation = tbl_location.objects.get(location_id=request.POST.get("sel_to_location"))
        uid = tbl_user.objects.get(user_id=request.session['uid'])
        cid = tbl_company.objects.get(company_id=cid)
        tbl_transport_request.objects.create(
            transport_request_description=request.POST.get('txt_request_description'),
            transport_request_qty=request.POST.get('txt_request_qty'),
            transport_request_for_date=request.POST.get('txt_request_for_date'),     
            user_id=uid,
            from_location_id=selectedFromLocation,
            to_location_id=selectedToLocation,
            company_id=cid,
            delivery_time=request.POST.get('txt_delivery_time'),
            delivery_date=request.POST.get('txt_delivery_date'),
            category_id=selectedCategory,
        )
        return render(request, "User/SendRequest.html", {"category" : category,'state':state})
    else:
        return render(request, "User/SendRequest.html", {"category" : category,'state':state})


def ViewRequest(request):
    uid = tbl_user.objects.get(user_id=request.session['uid'])
    requestData = tbl_transport_request.objects.filter(user_id=uid)
    return render(request,"User/ViewRequest.html",{'requestData':requestData})




def Logout(request):
    del request.session["did"]
    return redirect("guest:Login")