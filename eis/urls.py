from django.conf.urls import include,url
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^sensor/', include('project.urls')),
    url(r'^admin/', admin.site.urls),
    
    url(r'^', include('project.urls')),

]