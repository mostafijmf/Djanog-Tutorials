from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    # return HttpResponse("This app home page.")
    return render(req, 'first_app/home.html')