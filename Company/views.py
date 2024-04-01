from django.shortcuts import render,redirect
from Admin.models import *
from Company.models import *


def HomePage(request):
    return render(request,"Company/HomePage.html")

def NewVehicle(request):
    type = tbl_vehicletype.objects.all()
    if request.method == "POST":
        subtype = tbl_vehiclesubtype.objects.get(vehiclesubtype_id=request.POST.get("sel_vehiclesubtype"))
        cid = tbl_company.objects.get(company_id=request.session["cid"])
        tbl_vehicle.objects.create(
            vehicle_chase_no=request.POST.get('txt_vehicle_chase_no'),
            vehicle_reg_no=request.POST.get('txt_vehicle_reg_no'),
            vehicle_insurance_date=request.POST.get('txt_vehicle_insurance_date'),
            vehicle_insurance_exp=request.POST.get('txt_vehicle_insurance_exp'),
            vehiclesubtype_id=subtype,
            company_id=cid,
            vehicle_detailes=request.POST.get('txt_vehicle_detailes'),
            vehicle_name=request.POST.get('txt_vehicle_name'),
            vehicle_amount=request.POST.get('txt_vehicle_amount'),
            vehicle_capacity=request.POST.get('txt_vehicle_capacity'),
        )
        return render(request, "Company/NewVehicle.html", {"type" : type})
    else:
        return render(request, "Company/NewVehicle.html", {"type" : type})
    

def VehicleList(request):
    cid = tbl_company.objects.get(company_id=request.session["cid"])
    vehicles = tbl_vehicle.objects.filter(company_id=cid)
    return render(request, "Company/VehicleList.html", {"vehicles" : vehicles})
    
def DriverRequest(request):
    cid = tbl_company.objects.get(company_id=request.session["cid"])
    driverRequest = tbl_driver_request.objects.filter(company_id=cid)
    return render(request, "Company/DriverRequest.html", {"driverRequest" : driverRequest})

def DriverRequestAccept(request,aid):
    cid = tbl_company.objects.get(company_id=request.session["cid"])
    drData=tbl_driver_request.objects.get(request_id=aid)
    did = tbl_driver.objects.get(driver_id=drData.driver_id.driver_id)
    tbl_company_driver.objects.create(
        company_id=cid,
        driver_id=did
    )
    drData.request_status=1
    drData.save()
    return redirect("company:DriverRequest")


def DriverRequestReject(request,rid):
    drData=tbl_driver_request.objects.get(request_id=rid)
    drData.request_status=2
    drData.save()
    return redirect("admin:DriverRequest")


def TransportationRequest(request):
    cid = tbl_company.objects.get(company_id=request.session['cid'])
    requestData = tbl_transport_request.objects.filter(company_id=cid)
    return render(request, "Company/ViewRequest.html", {"requestData" : requestData})

def TransportationRequestAccept(request,aid):
    driver = tbl_driver.objects.all()
    vehicle = tbl_vehicle.objects.all()
    if request.method == "POST":
        trData=tbl_transport_request.objects.get(transport_request_id=aid)
        did1=tbl_driver.objects.get(driver_id=request.POST.get("sel_driver_1"))
        did2=tbl_driver.objects.get(driver_id=request.POST.get("sel_driver_2"))
        vid=tbl_vehicle.objects.get(vehicle_id=request.POST.get("sel_vehicle"))
        tbl_transport_shedule.objects.create(
            transport_request_id=trData,
            driver_1_id=did1,
            driver_2_id=did2,
            vehicle_id =vid
        )
        trData.transport_request_status=2
        trData.save()
        return redirect("company:TransportationRequest")
    return render(request, "Company/SheduleRequest.html", {"driver" : driver,'vehicle':vehicle})


def TransportationRequestReject(request,rid):
    drData=tbl_transport_request.objects.get(transport_request_id=rid)
    drData.transport_request_status=1
    drData.save()
    return redirect("company:TransportationRequest")
    

def Logout(request):
    del request.session["cid"]
    return redirect("guest:Login")