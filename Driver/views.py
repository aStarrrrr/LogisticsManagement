from django.shortcuts import render,redirect
from Admin.models import *
from Driver.models import *
from Company.models import *
from User.models import *
from Guest.models import *
from django.http import JsonResponse
from .utils import dijkstra

def HomePage(request):
    return render(request,"Driver/HomePage.html")

def DriverLicense(request):
    data = tbl_driver_license.objects.all()
    if request.method == "POST" and request.FILES:
        did = tbl_driver.objects.get(driver_id=request.session['did'])
        tbl_driver_license.objects.create(
            driver_license_exp_date=request.POST.get('txt_exp_date'),
            driver_license_badge_exp_date=request.POST.get('txt_badge_exp_date'),
            driver_license_class=request.POST.get('txt_class'),
            driver_license_number=request.POST.get('txt_number'),     
            driver_license_front_photo=request.FILES.get('file_front_photo'),
            driver_license_back_photo=request.FILES.get('file_back_photo'),
            driver_id=did,
        )
        return render(request, "Driver/DriverLicense.html", {"data" : data})
    else:
        return render(request, "Driver/DriverLicense.html", {"data" : data})

def DeleteDriverLicense(request,id):
    tbl_driver_license.objects.get(driving_license_id=id).delete()
    return redirect("driver:DriverLicense")

def SearchCompany(request):
    state = tbl_state.objects.all()
    return render(request,"Driver/SearchCompany.html",{'state':state})

def SendRequest(request,cid):
    cid = tbl_company.objects.get(company_id=cid)
    did = tbl_driver.objects.get(driver_id=request.session['did'])
    tbl_driver_request.objects.create(
        company_id=cid,
        driver_id=did
    )
    return render(request,"Driver/HomePage.html")


def ViewRequest(request):
    did = tbl_driver.objects.get(driver_id=request.session['did'])
    requestData = tbl_driver_request.objects.filter(driver_id=did)
    return render(request,"Driver/ViewRequest.html",{'requestData':requestData})


def AssignedTrip(request):
    did = tbl_driver.objects.get(driver_id=request.session['did'])
    data = tbl_transport_shedule.objects.filter(driver_1_id=did) | tbl_transport_shedule.objects.filter(driver_2_id=did)
    return render(request,"Driver/AssignedTrip.html",{'data':data})

def AssignedUpdate(request,id,sts):
    data = tbl_transport_request.objects.get(transport_request_id=id)
    data.transport_request_status=sts
    data.save()
    return redirect("driver:AssignedTrip")


def shortest_path(request, start_id, end_id):
    start_location = tbl_location.objects.get(location_id=start_id)
    end_location = tbl_location.objects.get(location_id=end_id)
    
    # Build graph
    graph = {}
    for route in tbl_route.objects.all():
        if route.from_location_id not in graph:
            graph[route.from_location_id] = {}
        graph[route.from_location_id][route.to_location_id] = route.route_distance
    
    # Find shortest path
    distances = dijkstra(graph, start_location)
    shortest_distance = distances[end_location]

    return {'start_location': start_location,'end_location': end_location,'shortest_distance': shortest_distance}


def AjaxUpdate(request):
    id = tbl_transport_shedule.objects.get(trasport_shedule_id=request.GET.get("id"))
    tbl_transport_update.objects.create(
        transport_shedule_id = id,
        transport_update_latitude = request.GET.get("longitude"),
        transport_update_longitude = request.GET.get("latitude")
    )
    return JsonResponse({"msg":"success"})


def Logout(request):
    del request.session["did"]
    return redirect("guest:Login")