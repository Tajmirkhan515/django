Installation of Django Framework using Visual Studio Code

Step 1: Install Django:
	pip install django

Step 2: Create a project:
	django-admin startproject myproject

Step 3: Change the current directory(optional):
	import os
	os.chdir('myproject')

Step 4: Now create an app in the project. Each project can consist of multiple apps:
	python manage.py startapp Testapp

Step 5: You can check and run the server:
	python manage.py runserver

Step 6: Enter the IP and port number to access the basic "successful page":
	http://127.0.0.1:8000/

Step 7: Add the app name in the settings file, more specifically in INSTALLED_APPS:
	INSTALLED_APPS = [
	'Testapp',
	]

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


Let's start coding
Step 1: Write something new in the views file (views.py):
	from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello, this is MyApp!")

Step 2: Add the URL in myproject's urls.py:
	from django.contrib import admin
	from django.urls import path, include
	from Testapp.views import home

	urlpatterns = [
	path('', home, name="home"),
	]