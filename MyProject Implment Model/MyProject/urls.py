from django.contrib import admin
from django.urls import path, include
from MyApp.views import *

urlpatterns = [
     path('', person_list, name='person_list'),
    path('add/', add_person, name='add_person'),

    path('admin/', admin.site.urls),


]
