from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

#String Message
def test_api(request):
    return HttpResponse("First API")

#Json Message

def test_json_api(request):
    data={
        "name":"First Json API",
        "Framework":"Python-Django"
    }
    return JsonResponse(data)
#Html
def test_html_page(request):
    context = {
        "name" : "Sit",
        "framework2024" : "Python-Django",
        "framework2023" : "Java-Spring-Boot",
        "year" : 2025   
    }
    return render(request,"index.html",context)

#Hello, {{name}}
def test_hello_name(request,name):
    return HttpResponse(f"Hello,{name}")



def test_html_for_page(request):
    context={
        "data":[
            {
        "name":"Sit",
        "Framework":"Python-Django",
        "year":2023
            },{

        "name":"sit",
        "Framework":"Java-Spring-Boot",
        "year":2022
            }
        ]
    }
    return render(request,"loop.html",context)

def home_page(request):
    return render(request,"home.html")

def home_page(request):
    context = {
        "page_data" : "Home Page"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    #print(request.GET['brand_name'])
    context = {
        "page_data" : "About Page"
    }
    return render(request, "home_page.html", context)