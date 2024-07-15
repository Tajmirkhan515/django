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

////////////////////////////////////////////////////////////////////////////////////////////////////

In the "MyProject Implment Model", i use a model, to create a form, to takes input from user and disply, using html pages

 	Model implementation
	
Step1: create a model.py file, write the code like below.	
 	from django.db import models

	# Create your models here.
	from django.db import models

	class Person(models.Model):
  	  first_name = models.CharField(max_length=100)
  	  last_name = models.CharField(max_length=100)
  	  age = models.IntegerField()
   	  semester = models.CharField(max_length=10)
	
Step2: 	Go to the admin.py file, and write the follwing code, 
	from django.contrib import admin
	from .models import Person

	admin.site.register(Person)

Step3:  use these two commands
	python manage.py makemigrations
        python manage.py migrate

Step4: this is the view files, where i create two methods

from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Person


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

def add_person(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        semester = request.POST.get('semester')
        
        if first_name and last_name and age and semester:
            Person.objects.create(first_name=first_name, last_name=last_name, age=age, semester=semester)
            return redirect('person_list')
    
    return render(request, 'add_person.html')


Step5: these are the HTML pages.
   ******add_person.html*********
<!DOCTYPE html>
<html>
<head>
    <title>Add Person</title>
    <script>
        function showAlert(message) {
            alert(message);
        }
    </script>
</head>
<body>
    <h1>Add Person</h1>
    <form method="post">
        {% csrf_token %}
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name"><br><br>
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name"><br><br>
        <label for="age">Age:</label>
        <input type="number" id="age" name="age"><br><br>
        <label for="semester">Semester:</label>
        <input type="text" id="semester" name="semester"><br><br>
        <button type="submit">Add Person</button>
    </form>
    <button type="button" onclick="showAlert('Hello')">Alert</button>
    <a href="{% url 'person_list' %}">Back to List</a>
</body>
</html>

         ****************person_list.html****************
<!DOCTYPE html>
<html>
<head>
    <title>Person List</title>
</head>
<body>
    <h1>Person List</h1>
    <ul>
        {% for person in persons %}
            <li>{{ person.first_name }} {{ person.last_name }} - {{ person.age }} - {{ person.semester }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'add_person' %}">Add Person</a>
</body>
</html>


==================================RecipePro=================================
RecipePro app, using djanog