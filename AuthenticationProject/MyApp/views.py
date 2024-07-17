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


