from django.http import HttpResponse
from django.shortcuts import render





from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

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
