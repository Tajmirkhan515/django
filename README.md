## Django Project Setup and Implementation Guide

### Installation and Setup

1. **Install Django**
    ```bash
    pip install django
    ```

2. **Create a Project**
    ```bash
    django-admin startproject myproject
    ```

3. **Change the Current Directory (Optional)**
    ```python
    import os
    os.chdir('myproject')
    ```

4. **Create an App in the Project**
    ```bash
    python manage.py startapp Testapp
    ```

5. **Check and Run the Server**
    ```bash
    python manage.py runserver
    ```

6. **Access the Basic "Successful Page"**
    Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

7. **Add the App Name in `settings.py`**
    ```python
    INSTALLED_APPS = [
        'Testapp',
    ]
    ```

---

### Coding

1. **Write Code in `views.py`**
    ```python
    from django.http import HttpResponse

    def home(request):
        return HttpResponse("Hello, this is MyApp!")
    ```

2. **Add URL in `myproject/urls.py`**
    ```python
    from django.contrib import admin
    from django.urls import path
    from Testapp.views import home

    urlpatterns = [
        path('', home, name="home"),
    ]
    ```

---

### Model Implementation

1. **Create `models.py`**
    ```python
    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        age = models.IntegerField()
        semester = models.CharField(max_length=10)
    ```

2. **Register the Model in `admin.py`**
    ```python
    from django.contrib import admin
    from .models import Person

    admin.site.register(Person)
    ```

3. **Apply Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create Views in `views.py`**
    ```python
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
    ```

5. **Create HTML Pages**

    **`add_person.html`**
    ```html
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
    ```

    **`person_list.html`**
    ```html
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
    ```

--- 

### RecipePro App

1. **Set Static URL in `settings.py`**
    ```python
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "public/static"),
    ]

    MEDIA_ROOT = os.path.join(BASE_DIR, "public/static")
    MEDIA_URL = '/media/'
    ```

---

### Authentication Project

1. **Define `MyApp` in `INSTALLED_APPS`**
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'MyApp',
    ]
    ```

2. **Update Templates List in `settings.py`**
    ```python
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
    ```

3. **Create Views in `views.py`**
    ```python
    from django.shortcuts import render, redirect
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth import login, logout

    from .middlewares import auth, guest

    @guest
    def register_view(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('dashboard')
        else:
            initial_data = {'username': '', 'password1': '', 'password2': ''}
            form = UserCreationForm(initial=initial_data)

        return render(request, 'auth/register.html', {'form': form})

    @guest
    def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('dashboard')
        else:
            initial_data = {'username': '', 'password1': ''}
            form = AuthenticationForm(initial=initial_data)

        return render(request, 'auth/login.html', {'form': form})

    @auth
    def dashboard_view(request):
        return render(request, 'dashboard.html')

    def logout_view(request):
        logout(request)
        return redirect('login')
    ```

4. **Update `urls.py`**
    ```python
    urlpatterns = [
        path('register/', register_view, name='register'),
        path('login/', login_view, name='login'),
        path('logout/', logout_view, name='logout'),
        path('dashboard/', dashboard_view, name='dashboard'),
    ]
    ```

5. **Update `models.py`**
    ```python
    from django.contrib.auth.models import User
    ```

6. **Create Template Files**

    **`layouts/app.html`**
    ```html
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
    ```

    **`auth/login.html`**
    ```html
    {% extends 'layouts/app.html' %}

    {% block content %}
    <div class="row justify-content-center">
        <div class="col-sm-6">
            <h2 class="text-muted">Login</h2>

            {% if form.non_field_errors %}
            <small class="text-danger">
                {{ form.non_field_errors.as_ul }}
            </small>
            {% endif %}

            <form method="POST" action="{% url 'login' %}">
                {% csrf_token %}
