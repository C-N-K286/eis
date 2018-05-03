from django.conf.urls import include,url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index ,name = "index"),

    url(r'^login_access/$', views.access, name='access'),
    url(r'^login/$', views.signIn, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),


    url(r'^index/$', views.index ,name = "index"),
    #url(r'^about.html/index.html/$', views.index ,name = "index"),
    url(r'^get/$', views.getdata ,name ="get"),
    url(r'^about/$', views.dashboard ,name ="dashboard"),
    url(r'^chart/$', views.chart ,name ="chart"),
    url(r'^check/$', views.check ,name ="check"),
	url(r'^contact/$', views.contact ,name ="contact"),  
    url(r'^test/$', views.test ,name ="test"),   
    url(r'^data/$', views.data ,name ="data"),
]
