from django.urls import path,include
from User import views
app_name = "user"
urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('SearchCompany/',views.SearchCompany,name="SearchCompany"),
    path('SendRequest/<int:cid>',views.SendRequest,name="SendRequest"),
    path('ViewRequest/',views.ViewRequest,name="ViewRequest"),
    path('Logout/',views.Logout,name="Logout"), 
]
