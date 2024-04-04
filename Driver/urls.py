from django.urls import path
from Driver import views
app_name = "driver"
urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('DriverLicense/',views.DriverLicense,name="DriverLicense"),
    path('DeleteDriverLicense/<int:id>',views.DeleteDriverLicense,name="DeleteDriverLicense"),
    path('SearchCompany/',views.SearchCompany,name="SearchCompany"),
    path('SendRequest/<int:cid>',views.SendRequest,name="SendRequest"),
    path('ViewRequest/',views.ViewRequest,name="ViewRequest"),
    path('AssignedTrip/',views.AssignedTrip,name="AssignedTrip"),
    path('AssignedUpdate/<int:id>/<int:sts>',views.AssignedUpdate,name="AssignedUpdate"),
    path('AjaxUpdate/',views.AjaxUpdate,name="AjaxUpdate"),
    path('Logout/',views.Logout,name="Logout"), 
]
