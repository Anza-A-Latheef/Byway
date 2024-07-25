from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def pageRoute(request):
    return render(request, "singlepage.html")

def listCourses(request):
    return render(request,"coursespage.html")