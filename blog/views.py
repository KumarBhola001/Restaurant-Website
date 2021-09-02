from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'blog/index.html')


def specific(request):
    list=[2,5,8,0]
    return HttpResponse(list)

def menu(request):
    return render(request,'blog/menu.html')
def specials(request):
    return render (request,'blog/specials.html')
def meals(request):
    return HttpResponse("Happy Meals")
def contact(request):
    return render(request,'blog/contact.html')
def about(request):
    return render(request,'blog/about.html')
