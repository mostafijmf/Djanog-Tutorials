from django.http import HttpResponse


def home(req):
    return HttpResponse("This is Home page.")


def contact(req):
    return HttpResponse("This is contact page.")
