from django.shortcuts import render,redirect
from Admin.models import *
from Driver.models import *
from Company.models import *
from User.models import *
from Guest.models import *
from django.http import JsonResponse
import heapq
from decimal import Decimal


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        # print(distances)
        # if current_distance > distances[current_node]:
        #     continue
        # for neighbor, weight in graph[current_node].items():
        #     distance = current_distance + weight
        #     if distance < distances[neighbor]:
        #         distances[neighbor] = distance
        #         heapq.heappush(queue, (distance, neighbor))
    
    return distances



def shortest_path(start_id, end_id):
    dataFrom = tbl_points.objects.filter(location_id=start_id)
    dataTo = tbl_points.objects.filter(location_id=end_id)

    common_route_ids = dataFrom.values_list('route_id', flat=True).intersection(dataTo.values_list('route_id', flat=True))
    common_route_ids_list = list(common_route_ids)
    print('common_route_ids_list:', common_route_ids_list)

    graph = {}
    for route_id in common_route_ids_list:
        route_data = tbl_points.objects.filter(route_id=route_id)
        graph[route_id] = {}
        for point in route_data:
            graph[route_id][point.location_id.location_id] = point.points_distance

    print('graph:', graph)

    sums = {}
    for main_node, sub_nodes in graph.items():
        total = sum(sub_nodes.values())
        sums[main_node] = total

    min_node = min(sums, key=sums.get)
    print("Node with the least sum:", min_node)

    distances = dijkstra(graph, start_id)
    shortest_distance = distances[end_id]

    return {'shortest_distance': shortest_distance}




def ViewMore(request,tid):
    data = tbl_transport_request.objects.get(transport_request_id=tid)
    start_id = data.from_location_id.location_id
    end_id = data.to_location_id.location_id
    shortest_path(start_id,end_id)
    return render(request,"Driver/ViewMore.html",{'data':data})




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

def AjaxUpdate(request):    
    id = tbl_transport_request.objects.get(transport_request_id=request.GET.get("id"))
    tbl_transport_update.objects.create(
        transport_request_id = id,
        transport_update_latitude = request.GET.get("latitude"),
        transport_update_longitude = request.GET.get("longitude")
    )
    return JsonResponse({"msg":"success"})


def Logout(request):
    del request.session["did"]
    return redirect("guest:Login")