from django.shortcuts import render

def home(request):
    return render(request,"home.html")
# Create your views here.
def about(request):
    return render(request,"about.html")
