 Instalation of django framwork using virtual studio, 
Step 1: pip install django
	After installation of django,

Step 2:  create a project:
	!django-admin startproject myproject

Step 3: change the current directory
	import os
 	os.chdir('CodePro')

Step 4: Now create a app in project, each project can consists of multiple app. 
 	!python manage.py startapp Testapp

Step 5: you can check the, and run a server. 
	!python manage.py runserver

Step 6: Enter IP and port number to access the basic "successfull page"
	http://127.0.0.1:8000/

Step 7: add Testapp name in setting file, more specificlly in INSTALLED_APPS =["Testapp"]


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Let's start to code. 

step 1: Let's write something new in view file. 

	---views.py

	from django.http import HttpResponse

	def home(request):
	    return HttpResponse("Hello, this is MyApp!")


Step 2: put url in MyProject urls.py 

	from django.contrib import admin
	from django.urls import path, include
	from MyApp.views import *

	urlpatterns = [
	    path('', home, name="home"),
	    #path('admin/', admin.site.urls),
	]
