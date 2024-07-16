from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def receipes(request):
    if request.method=="POST":
        data=request.POST
        reciepe_image=request.FILES.get('reciepe_image')
        
        reciepe_descr=data.get('reciepe_descr')
        reciepe_name=data.get('reciepe_name')
        Receipe.objects.create(
            reciepe_image=reciepe_image,
            reciepe_name=reciepe_name,
            reciepe_descr=reciepe_descr,
        )

    queryset=Receipe.objects.all()

    #this is for search
    if request.GET.get('search'):
        print(request.GET.get('search'))  #__icontains is a django keyword
        queryset=queryset.filter(reciepe_name__icontains=request.GET.get('search'))

    context={'receipes': queryset}

    return render(request, 'receipes.html',context)


def delete_receipe( request, id):
    print("this is id", id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)

    if request.method=='POST':
        data=request.POST

        reciepe_image=request.FILES.get('reciepe_image')
        reciepe_name=data.get('reciepe_name')
        reciepe_descr=data.get('reciepe_descr')

        queryset.reciepe_name=reciepe_name
        queryset.reciepe_descr=reciepe_descr

        if reciepe_image:
            queryset.reciepe_image=reciepe_image

        queryset.save()
        return redirect('/receipes/')
    context={'receipe':queryset}
    #
    return render(request, 'update_receipes.html',context)

