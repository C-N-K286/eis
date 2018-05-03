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

# Create your views here
def index(request):
	data = []
	for i in range(1,10):
		obj = sensor.objects.all()[len(sensor.objects.all()) - i]
		data.append(obj.sensor_value)
	data = [list(map(int, x)) for x in data]
	context={'data' : data}
	return render(request,'project/index.html',context)

def getdata(request):
	if request.method=='GET' :
		data = request.GET['value']
		obj=sensor()
		obj.sensor_value=data
		obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")


@login_required(login_url='/sensor/login_access')	
def dashboard(request):
	context = {}
	return render(request,'project/about.html',context)

def chart(request):
	data = []
	for i in range(1,10):
		obj = sensor.objects.all()[len(sensor.objects.all()) - i]
		data.append(obj.sensor_value)
	data = [list(map(int, x)) for x in data]
	context={'data' : data}
	return render(request,'project/chart.html',context)


def check(request):
	data = []
	for i in range(1,10):
		obj = sensor.objects.all()[len(sensor.objects.all()) - i]
		data.append(obj.sensor_value)
	data = [list(map(int, x)) for x in data]
	context={'data' : data}
	return render(request,'project/check.html',context)



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



def test(request):
	context = {}
	return render(request,'project/test.html',context)

