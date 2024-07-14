from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    return HttpResponse("""<h1>Hello, this is MyApp!</h1>
     <p> this is pargraph tags</p>
     </hr>
     <h2 style="color:red"> this is H2 heading</h2>
    """)


def next(request):

    return HttpResponse("<h1> Hello this is html tag of h1</h1>")


def rtnhtml(request):
    return render(request,"index.html")


def passDataToHtml(request):
    Peoples=[
        {'name':"kashi",'age':26},
        {'name':"khalid",'age':29},
        {'name':"kashi",'age':96},
        {'name':"naveed",'age':86},
        {'name':"kashi",'age':26},
        {'name':"khan",'age':26},
        {'name':"kashi",'age':36},
    ]

    text="Hello this text from view file, and recived and in the cathdata html"
    return render (request,"catchdata.html",context={'peoples':Peoples, 'txt':text})