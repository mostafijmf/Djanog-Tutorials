from django.shortcuts import render

from django.http import HttpResponse


def courses(req):
    return HttpResponse("This is Courses page.")
