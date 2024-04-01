from django.urls import path,include
from Company import views
app_name = "company"
urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('NewVehicle/',views.NewVehicle,name="NewVehicle"),
    path('VehicleList/',views.VehicleList,name="VehicleList"),

    path('DriverRequest/',views.DriverRequest,name="DriverRequest"),
    path('DriverRequestAccept/<int:aid>',views.DriverRequestAccept,name="DriverRequestAccept"),
    path('DriverRequestReject/<int:rid>',views.DriverRequestReject,name="DriverRequestReject"),

    path('TransportationRequest/',views.TransportationRequest,name="TransportationRequest"),
    path('TransportationRequestAccept/<int:aid>',views.TransportationRequestAccept,name="TransportationRequestAccept"),
    path('TransportationRequestReject/<int:rid>',views.TransportationRequestReject,name="TransportationRequestReject"),


    path('Logout/',views.Logout,name="Logout"),
]
