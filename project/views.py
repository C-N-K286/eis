# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import sensor
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect


from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from random import randint
# Create your views here
def index(request):
	data = []
	for i in range(1,11):
		obj = sensor.objects.all()[len(sensor.objects.all()) - i]
		data.append(obj.sensor_value)
	data = [list(map(int, x)) for x in data]
	context={'data' : data}
	return render(request,'project/index.html',context)

def getdata(request):
	if request.method=='GET' :
		data = request.GET['temperature']
		data1 = request.GET['humidity']
		obj=sensor()
		obj.sensor_value=data
		obj.sensor_value1=data1
		obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")


@login_required(login_url='/sensor/login_access')	
def dashboard(request):
	temperature=[]
	humidity = []
	for i in range(1,11):
		obj = sensor.objects.all()[len(sensor.objects.all()) - i]
		print obj
		print obj.sensor_value,obj.sensor_value1
		#tem,hum = obj.split(" ")
		temperature.append(int(obj.sensor_value))
		humidity.append(int(obj.sensor_value1))
	context={'temperature' : temperature,'humidity':humidity}
	return render(request,'project/about.html',context)
def dashboardst2(request):
	temperature=[]
	humidity = []
	for i in range(1,11):
		temperature.append(randint(30,40))
		humidity.append(randint(60,70))
	context={'temperature' : temperature,'humidity':humidity}
	return render(request,'project/about.html',context)
def dashboardst3(request):
	temperature=[]
	humidity = []
	for i in range(1,11):
		temperature.append(randint(30,40))
		humidity.append(randint(60,70))
	context={'temperature' : temperature,'humidity':humidity}
	return render(request,'project/about.html',context)
@login_required(login_url='/sensor/login_access')	
def contact(request):
	context = {}
	return render(request,'project/contact.html',context)


def access(request):
	return render( request,'project/login.html')
	
def signIn(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		user = authenticate(username=username, password=password)
		print user
		if user is not None:
			if user.is_active:
				login(request, user)
				flag=1
				return redirect('/about')
			else:
				return redirect('/index')
		else:
			#return redirect('/index')
			return HttpResponse("Login Not Succesfull")
	return HttpResponse("Login!!!!! Not Succesfull")


#@login_required(login_url='/sensor/login_access')		
def logout_view(request):
	print "working"
	logout(request)
	return redirect('/')


