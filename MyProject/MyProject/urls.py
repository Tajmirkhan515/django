from django.contrib import admin
from django.urls import path, include
from MyApp.views import *

urlpatterns = [
    path('', home, name="home"),
    #path('admin/', admin.site.urls),
]
