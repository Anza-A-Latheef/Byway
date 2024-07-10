from django.shortcuts import render

def home(request):
    return render(request,"home.html")

# def clickbutton(request):
#     return render(request, "hh.html")