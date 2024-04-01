from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from django.db.models import Q

def HomePage(request):
    return render(request,"Guest/HomePage.html")

def CompanyRegistration(request):
    state = tbl_state.objects.all()
    if request.method == "POST" and request.FILES:
        location = tbl_location.objects.get(location_id=request.POST.get("sel_location"))
        tbl_company.objects.create(
            company_name=request.POST.get('txt_name'),
            company_contact=request.POST.get('txt_contact'),
            company_email=request.POST.get('txt_email'),
            company_address=request.POST.get('txt_address'),
            company_since=request.POST.get('txt_since'),     
            company_proof=request.FILES.get('file_proof'),
            company_logo=request.FILES.get('file_logo'),
            owner_name=request.POST.get('txt_oname'),
            owner_email=request.POST.get('txt_oemail'),
            owner_contact=request.POST.get('txt_ocontact'),
            company_password=request.POST.get('txt_password'),
            location_id=location,
        )
        return render(request, "Guest/CompanyRegistration.html", {"state" : state})
    else:
        return render(request, "Guest/CompanyRegistration.html", {"state" : state})

def DriverRegistration(request):
    state = tbl_state.objects.all()
    if request.method == "POST" and request.FILES:
        location = tbl_location.objects.get(location_id=request.POST.get("sel_location"))
        tbl_driver.objects.create(
            driver_name=request.POST.get('txt_name'),
            driver_primary_contact=request.POST.get('txt_contact1'),
            driver_secondary_contact=request.POST.get('txt_contact2'),
            driver_email=request.POST.get('txt_email'),     
            driver_proof=request.FILES.get('file_proof'),
            driver_photo=request.FILES.get('file_photo'),
            driver_dob=request.POST.get('txt_dob'),
            driver_address=request.POST.get('txt_address'),
            driver_password=request.POST.get('txt_password'),
            driver_expirence=request.POST.get('txt_expirence'),
            location_id=location,
        )
        return render(request, "Guest/DriverRegistration.html", {"state" : state})
    else:
        return render(request, "Guest/DriverRegistration.html", {"state" : state})
    
def UserRegistration(request):
    state = tbl_state.objects.all()
    if request.method == "POST":
        location = tbl_location.objects.get(location_id=request.POST.get("sel_location"))
        tbl_user.objects.create(
            user_name=request.POST.get('txt_name'),
            user_contact=request.POST.get('txt_contact'),
            user_email=request.POST.get('txt_email'),
            user_dob=request.POST.get('txt_dob'),
            user_address=request.POST.get('txt_address'),
            user_password=request.POST.get('txt_password'),
            user_aadhar_number=request.POST.get('txt_aadhar'),
            location_id=location,
        )
        return render(request, "Guest/UserRegistration.html", {"state" : state})
    else:
        return render(request, "Guest/UserRegistration.html", {"state" : state})
    

def Login(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        AdminCount =  tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        UserCount =  tbl_user.objects.filter(user_email=email,user_password=password).count()
        CompanyCount =  tbl_company.objects.filter(Q(company_email=email) | Q(owner_email=email),company_password=password).count()
        DriverCount =  tbl_driver.objects.filter(driver_email=email,driver_password=password).count()
        if AdminCount > 0:
            admin = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"] = admin.admin_id
            return redirect("admin:HomePage")
        elif CompanyCount > 0:
            company = tbl_company.objects.get(Q(company_email=email) | Q(owner_email=email),company_password=password)
            request.session["cid"] = company.company_id
            return redirect("company:HomePage")
        elif DriverCount > 0:
            driver = tbl_driver.objects.get(driver_email=email,driver_password=password)
            request.session["did"] = driver.driver_id
            return redirect("driver:HomePage")
        elif UserCount > 0:
            user = tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"] = user.user_id
            return redirect("user:HomePage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")