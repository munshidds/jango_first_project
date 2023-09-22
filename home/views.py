from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("this is home page")
def about(request):
    return HttpResponse("this is about page")
def booking(request):
    return HttpResponse("this is booking page")
def doctors(request):
    return HttpResponse("this is doctorts page")
def condact(request):
    return HttpResponse("this is condact page")