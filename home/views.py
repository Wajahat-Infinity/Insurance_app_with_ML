from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def prediction(request):
    return render(request,"prediction.html")

def contact(request):
    return render(request,"contact.html")