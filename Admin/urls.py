from django.urls import path
from Admin import views
app_name = "admin"
urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),

    path('AjaxVehicleSubType/',views.AjaxVehicleSubType,name="AjaxVehicleSubType"),
    path('AjaxDistrict/',views.AjaxDistrict,name="AjaxDistrict"),
    path('AjaxLocation/',views.AjaxLocation,name="AjaxLocation"),
    path('AjaxCompany/',views.AjaxCompany,name="AjaxCompany"),
    path('AjaxCompanyUser/',views.AjaxCompanyUser,name="AjaxCompanyUser"),

    path('NewState/',views.NewState,name="NewState"),
    path('DeleteState/<int:did>',views.DeleteState,name="DeleteState"),
    path('EditState/<int:eid>',views.EditState,name="EditState"),

    path('NewRoute/',views.NewRoute,name="NewRoute"),
    path('DeleteRoute/<int:did>',views.DeleteRoute,name="DeleteRoute"),
    path('EditRoute/<int:eid>',views.EditRoute,name="EditRoute"),
    
    path('NewDistrict/',views.NewDistrict,name="NewDistrict"),
    path('DeleteDistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('EditDistrict/<int:eid>',views.EditDistrict,name="EditDistrict"),

    path('NewLocation/',views.NewLocation,name="NewLocation"),
    path('DeleteLocation/<int:did>',views.DeleteLocation,name="DeleteLocation"),

    path('NewVehicleType/',views.NewVehicleType,name="NewVehicleType"),
    path('DeleteVehicleType/<int:did>',views.DeleteVehicleType,name="DeleteVehicleType"),
    path('EditVehicleType/<int:eid>',views.EditVehicleType,name="EditVehicleType"),

    path('NewVehicleSubType/',views.NewVehicleSubType,name="NewVehicleSubType"),
    path('DeleteVehicleSubType/<int:did>',views.DeleteVehicleSubType,name="DeleteVehicleSubType"),
    path('EditVehicleSubType/<int:eid>',views.EditVehicleSubType,name="EditVehicleSubType"),

    path('NewCategory/',views.NewCategory,name="NewCategory"),
    path('DeleteCategory/<int:did>',views.DeleteCategory,name="DeleteCategory"),
    path('EditCategory/<int:eid>',views.EditCategory,name="EditCategory"),

    path('NewPoints/',views.NewPoints,name="NewPoints"),
    path('DeletePoints/<int:did>',views.DeletePoints,name="DeletePoints"),


    path('Logout/',views.Logout,name="Logout"),

    
]
