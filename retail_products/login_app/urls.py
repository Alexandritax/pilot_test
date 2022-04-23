from django.urls import path
from login_app import views

urlpatterns = [

    path('main/', views.print_world, name= "Main")
    

]