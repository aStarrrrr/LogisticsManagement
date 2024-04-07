from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Company.models import *
from Driver.models import *
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

def TransportProgress(request,id):
    request_id = tbl_transport_request.objects.get(transport_request_id=id)
    transport_updates = tbl_transport_update.objects.filter(transport_request_id=request_id)
    transport_update_data = [{
        'latitude': update.transport_update_latitude,
        'longitude': update.transport_update_longitude
    } for update in transport_updates]
    print(transport_update_data)
    return render(request, 'User/TransportProgress.html', {'transport_update_data': transport_update_data})




def Logout(request):
    del request.session["uid"]
    return redirect("guest:Login")