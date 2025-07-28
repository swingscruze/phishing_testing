from django.shortcuts import render, HttpResponse

# Create your views here.



def home(request):
    return HttpResponse("hello welcome home")


def deleteuser(request):

    return HttpResponse("time to delet user")


def adduser(request):

    return HttpResponse("time to adduser ")



