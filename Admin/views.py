from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

def HomePage(request):
    return render(request,"Admin/HomePage.html")

# Category Function Start

def NewCategory(request):
    category = tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get('txt_category'))
        return render(request,"Admin/Category.html",{'category':category})
    else:
        return render(request,"Admin/Category.html",{'category':category})
    
def DeleteCategory(request,did):
    tbl_category.objects.get(category_id=did).delete()
    return redirect("admin:NewCategory")

def EditCategory(request,eid):
    category = tbl_category.objects.all()
    editdata=tbl_category.objects.get(category_id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get('txt_category')
        editdata.save()
        return redirect("admin:NewCategory")
    else:
        return render(request,"Admin/Category.html",{'editdata':editdata,'category':category})
    
# Category Functions End

# Route Function Start

def NewRoute(request):
    route = tbl_route.objects.all()
    if request.method=="POST":
        tbl_route.objects.create(route_name=request.POST.get('txt_route'))
        return render(request,"Admin/Route.html",{'route':route})
    else:
        return render(request,"Admin/Route.html",{'route':route})
    
def DeleteRoute(request,did):
    tbl_route.objects.get(route_id=did).delete()
    return redirect("admin:NewRoute")

def EditRoute(request,eid):
    route = tbl_route.objects.all()
    editdata=tbl_route.objects.get(route_id=eid)
    if request.method=="POST":
        editdata.route_name=request.POST.get('txt_route')
        editdata.save()
        return redirect("admin:NewRoute")
    else:
        return render(request,"Admin/Route.html",{'editdata':editdata,'route':route})
    
# Route Functions End

# State Function Start

def NewState(request):
    state = tbl_state.objects.all()
    if request.method=="POST":
        tbl_state.objects.create(state_name=request.POST.get('txt_state'))
        return render(request,"Admin/State.html",{'state':state})
    else:
        return render(request,"Admin/State.html",{'state':state})
    
def DeleteState(request,did):
    tbl_state.objects.get(state_id=did).delete()
    return redirect("admin:NewState")

def EditState(request,eid):
    state = tbl_state.objects.all()
    editdata=tbl_state.objects.get(state_id=eid)
    if request.method=="POST":
        editdata.state_name=request.POST.get('txt_state')
        editdata.save()
        return redirect("admin:NewState")
    else:
        return render(request,"Admin/State.html",{'editdata':editdata,'state':state})
    
# State Functions End
    

# VehicleType Function Start

def NewVehicleType(request):
    vehicletype = tbl_vehicletype.objects.all()
    if request.method=="POST":
        tbl_vehicletype.objects.create(vehicletype_name=request.POST.get('txt_vehicletype'))
        return render(request,"Admin/VehicleType.html",{'vehicletype':vehicletype})
    else:
        return render(request,"Admin/VehicleType.html",{'vehicletype':vehicletype})
    
def DeleteVehicleType(request,did):
    tbl_vehicletype.objects.get(vehicletype_id=did).delete()
    return redirect("admin:NewVehicleType")

def EditVehicleType(request,eid):
    vehicletype = tbl_vehicletype.objects.all()
    editdata=tbl_vehicletype.objects.get(vehicletype_id=eid)
    if request.method=="POST":
        editdata.vehicletype_name=request.POST.get('txt_vehicletype')
        editdata.save()
        return redirect("admin:NewVehicleType")
    else:
        return render(request,"Admin/VehicleType.html",{'editdata':editdata,'vehicletype':vehicletype})
    
# VehicleType Functions End
    
# VehicleSubType functions Start
    
def NewVehicleSubType(request):
    vehiclesubtype=tbl_vehiclesubtype.objects.all()
    vehicletype=tbl_vehicletype.objects.all()
    if request.method=="POST":
        selectedState=tbl_vehicletype.objects.get(vehicletype_id=request.POST.get('sel_vehicletype'))
        tbl_vehiclesubtype.objects.create(vehiclesubtype_name=request.POST.get("txt_vehiclesubtype"),vehicletype_id=selectedState)
        return render(request,"Admin/VehicleSubType.html",{'vehicletype':vehicletype,'vehiclesubtype':vehiclesubtype})
    else:
        return render(request,"Admin/VehicleSubType.html",{'vehicletype':vehicletype,'vehiclesubtype':vehiclesubtype})
    
def DeleteVehicleSubType(request,did):
    tbl_vehiclesubtype.objects.get(vehiclesubtype_id=did).delete()
    return redirect("admin:NewVehicleSubType")


def EditVehicleSubType(request,eid):
    vehicletype=tbl_vehicletype.objects.all()
    vehiclesubtype = tbl_vehiclesubtype.objects.all()
    editdata=tbl_vehiclesubtype.objects.get(vehiclesubtype_id=eid)
    if request.method=="POST":
        editdata.vehiclesubtype_name=request.POST.get('txt_vehiclesubtype')
        editdata.vehicletype_id=tbl_vehicletype.objects.get(vehicletype_id=request.POST.get('sel_vehicletype'))
        editdata.save()
        return redirect("admin:NewVehicleSubType")
    else:
        return render(request,"Admin/VehicleSubType.html",{'editdata':editdata,'vehiclesubtype':vehiclesubtype,'vehicletype':vehicletype})

# VehicleSubType functions End
    

# Distrcit functions Start
    
def NewDistrict(request):
    district=tbl_district.objects.all()
    state=tbl_state.objects.all()
    if request.method=="POST":
        selectedState=tbl_state.objects.get(state_id=request.POST.get('sel_state'))
        tbl_district.objects.create(district_name=request.POST.get("txt_district"),state_id=selectedState)
        return render(request,"Admin/District.html",{'state':state,'district':district})
    else:
        return render(request,"Admin/District.html",{'state':state,'district':district})
    
def DeleteDistrict(request,did):
    tbl_district.objects.get(district_id=did).delete()
    return redirect("admin:NewDistrict")


def EditDistrict(request,eid):
    state=tbl_state.objects.all()
    district = tbl_district.objects.all()
    editdata=tbl_district.objects.get(district_id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get('txt_district')
        editdata.state_id=tbl_state.objects.get(state_id=request.POST.get('sel_state'))
        editdata.save()
        return redirect("admin:NewDistrict")
    else:
        return render(request,"Admin/District.html",{'editdata':editdata,'district':district,'state':state})

# Distrcit functions End



# Location functions Start
    
def NewLocation(request):
    location=tbl_location.objects.all()
    district=tbl_district.objects.all()
    state=tbl_state.objects.all()
    if request.method=="POST":
        selectedDistrict=tbl_district.objects.get(district_id=request.POST.get('sel_district'))
        tbl_location.objects.create(location_name=request.POST.get("txt_location"),district_id=selectedDistrict)
        return render(request,"Admin/Location.html",{'state':state,'district':district,'location':location})
    else:
        return render(request,"Admin/Location.html",{'state':state,'district':district,'location':location})
    
def DeleteLocation(request,did):
    tbl_location.objects.get(location_id=did).delete()
    return redirect("admin:NewLocation")


# Location functions End

def AjaxVehicleSubType(request):
    vehicletype=tbl_vehicletype.objects.get(vehicletype_id=request.GET.get("id"))
    vehiclesubtype=tbl_vehiclesubtype.objects.filter(vehicletype_id=vehicletype)
    return render(request,"Admin/AjaxVehicleSubType.html",{"vehiclesubtype" : vehiclesubtype})

def AjaxDistrict(request):
    state=tbl_state.objects.get(state_id=request.GET.get("sid"))
    district=tbl_district.objects.filter(state_id=state)
    return render(request,"Admin/AjaxDistrict.html",{"district" : district})

def AjaxLocation(request):
    district=tbl_district.objects.get(district_id=request.GET.get("did"))
    location=tbl_location.objects.filter(district_id=district)
    return render(request,"Admin/AjaxLocation.html",{"location" : location})

def AjaxCompany(request):
    location=tbl_location.objects.get(location_id=request.GET.get("lid"))
    company=tbl_company.objects.filter(location_id=location)
    return render(request,"Admin/AjaxCompany.html",{"company" : company})

def AjaxCompanyUser(request):
    location=tbl_location.objects.get(location_id=request.GET.get("lid"))
    company=tbl_company.objects.filter(location_id=location)
    return render(request,"Admin/AjaxCompanyUser.html",{"company" : company})

def NewPoints(request):
    route = tbl_route.objects.all()
    state = tbl_state.objects.all()
    points = tbl_points.objects.all()
    if request.method == "POST":
        selectedRoute=tbl_route.objects.get(route_id=request.POST.get("sel_route"))
        tbl_points.objects.create(points_distance=request.POST.get("txt_distance"),
                            points_name=request.POST.get("txt_name"),
                            points_order=request.POST.get("txt_order"),
                            route_id = selectedRoute,
                            from_location_id=tbl_location.objects.get(location_id=request.POST.get("sel_flocation")),
                            to_location_id=tbl_location.objects.get(location_id=request.POST.get("sel_tlocation")))
        return redirect("admin:NewPoints")
    else:
        return render(request,"Admin/Points.html",{"route":route,'points':points,'state':state})

def DeletePoints(request,did):
    tbl_points.objects.get(points_id=did).delete()
    return redirect("admin:NewPoints")
    
def Logout(request):
    del request.session["aid"]
    return redirect("guest:Login")