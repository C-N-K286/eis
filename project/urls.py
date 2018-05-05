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
    url(r'^get/$', views.getdata ,name ="get"),
    url(r'^about/$', views.dashboard ,name ="dashboard"),
    url(r'^about/st2/$', views.dashboardst2 ,name ="dashboardst2"),
    url(r'^about/st3/$', views.dashboardst3 ,name ="dashboardst3"),
	url(r'^contact/$', views.contact ,name ="contact"),  
]
