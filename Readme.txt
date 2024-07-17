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

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
In The complete recipe app, I add how to set static url, past the bolow code in the setting.py file
=> insert recipe
=> delete recipe
=> update recipe
=> search recipe
=> shows the whole recipes


How set a static url
import os

# Assuming BASE_DIR is defined above, like:
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "public/static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "public/static")
MEDIA_URL = '/media/'


//////////////////////////////////////////////////////////////////////////////////////////////////////

In the AuthenticationProject, we design the full registeratin, login page, and hanlde all operations. 

Step 1: define MyApp in INSTALLED_AP list,  in the setting file
 	INSTALLED_AP= INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MyApp',
]

Step 2: Update the Templates list, with accurate directory of of templates folder
	TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'MyApp' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



Step 3: this is my View.py files, consists of below code. 

from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout

from .middlewares import auth, guest


@guest
def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'', 'password1': '', 'password2': ''}
        form=UserCreationForm(initial=initial_data)

    return render(request,'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'', 'password1': ''}
        form=AuthenticationForm(initial=initial_data)

    return render(request,'auth/login.html',{'form':form})


@auth
def dashboard_view(request):
    return render(request,'dashboard.html')



def logout_view(request):
    logout(request)
    return redirect('login')


Stpe 3: update the url.py file

 
urlpatterns = [
   # path('', admin.site.urls),
    path('register/', register_view, name='register'), # type: ignore
    path('login/', login_view, name='login'), # type: ignore
    path('logout/', logout_view, name='logout'), # type: ignore
    path('dashboard/', dashboard_view, name='dashboard'), # type: ignore    
]


Step 4: update teh models.py files
  # Create your models here.

from django.contrib.auth.models import User


Step 5: i created the template files, with a following herarichy 

        templates/
           auth/
              login.html/
              register.html/
           layouts/
              app.html
        /dashboard.html

Step 6: apply the following comands
    python manage.py makemigrations
    python manage.py migrate


Step 7: The following html codes. 
     layouts/app.html

   <!DOCTYPE html>
<html lang="en">
<head>
  <title>Django Auth</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body style="padding: 10%;">

{% block content %}

{% endblock %}

</body>
</html>

***************login*******************
{% extends 'layouts/app.html' %}

{% block content %}


<div class="row justify-content-center">
    <div class="col-sm-6">
        <h2 class="text-muted">Login</h2>

        {% if form.non_field_errors %}

        <small class="text-danger">
         {{form.non_field_errors.as_ul}}
        </small>
      {% endif %}

        <form method="POST" action="{% url 'login' %}">
             {%csrf_token%}
             <div class="form-group">
                <label for="{{form.username.id_for_label}}">Username</label>
                <input type="text" name="{{form.username.name}}" class="form-control" value="{{form.username.value}}">
                <span class="text-danger">{{form.username.errors}}</span>
             </div>
            

             <div class="form-group">
                <label for="{{form.password.id_for_label}}">password</label>
                <input type="text" name="{{form.password.name}}" class="form-control" value="{{form.password.value}}">
                <span class="text-danger">{{form.password.errors}}</span>
             </div>
            


             
            
           <button type="submit" class="btn btn-dark">Login</button>
           <a href="{% url 'register' %}" class="btn btn-default">Create a new account</a>
        </form>
    </div>
</div>

{% endblock %}

*************registeration********************
{% extends 'layouts/app.html' %}

{% block content %}

<div class="row justify-content-center">
    <div class="col-sm-6">
        <h2 class="text-muted">Register</h2>
        <form method="POST" action="{% url 'register' %}">
             {%csrf_token%}
             <div class="form-group">
                <label for="{{form.username.id_for_label}}">Username</label>
                <input type="text" name="{{form.username.name}}" class="form-control" value="{{form.username.value}}">
                <span class="text-danger">{{form.username.errors}}</span>
             </div>
            

             <div class="form-group">
                <label for="{{form.password1.id_for_label}}">Password1</label>
                <input type="text" name="{{form.password1.name}}" class="form-control" value="{{form.password1.value}}">
                <span class="text-danger">{{form.password1.errors}}</span>
             </div>
            


             <div class="form-group">
                <label for="{{form.password2.id_for_label}}">Re-Type Password: </label>
                <input type="text" name="{{form.password2.name}}" class="form-control" value="{{form.password2.value}}">
                <span class="text-danger">{{form.password2.errors}}</span>
             </div>
            
           <button type="submit" class="btn btn-dark">Submit</button>
           <a href="{% url 'login' %}" class="btn btn-default">Login</a>
        </form>
    </div>
</div>

{% endblock %}


****************dashboard.py***************


{% extends 'layouts/app.html' %}


{% block content %}

    <h2> Dashboard : {{request.user.username}}</h2>
    <a href="{% url 'logout' %}" class="btn btn-dark">log out</a>


{% endblock %}


step 8: middlewares.py, this is very important code.

from django.shortcuts import redirect

def auth(view_function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated==False:
            return redirect('login')
        return view_function(request,*args,**kwargs)
    return wrapped_view



#*********Guest user**************
def guest(view_function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_function(request,*args,**kwargs)
    return wrapped_view