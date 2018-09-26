from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from fetching import *




def index(request, *args, **kwargs):
    Tempsoil= Temp_soil() # for y axis
    labels = Time() # for x axis
    Tempatm = Temp_atm() # for next chart
    Moisture1 = Moisture()
    Humidity1 = Humidity()
    fetch1 = Fetch1()
    fetch2 = Fetch2()
    fetch3 = Fetch3()
    fetch4 = Fetch4()

    return render(request, 'personal/charts.html', {"Soil_temp":Tempsoil,"Atm_Temp":Tempatm, "Moisture": Moisture1, "Humidity":Humidity1 ,"Time":labels, "Soil_fetch": fetch1 ,"Atm_fetch": fetch2,"Moisture_fetch":fetch3,"Humidity_fetch":fetch4})
def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})



