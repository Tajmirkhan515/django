from django.shortcuts import render
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
    return render(request, 'receipes.html')

