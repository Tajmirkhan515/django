from django.contrib import admin
from django.urls import path, include
from MyApp.views import *

urlpatterns = [
    path('', home, name="home"),
    path("next-page",next,name="next"),
    path("html-page",rtnhtml,name='html page'),
    path("people-list",passDataToHtml, name="People list"),
    path('admin/', admin.site.urls),
]
