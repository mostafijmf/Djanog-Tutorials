from django.shortcuts import render
import datetime


def about(req):
    me = {
        'name': 'Mostafij',
        'age': '23',
        'address': 'Cumilla',
        'gpa': 4.5,
        'courses': [
            'C', 'C++', 'Python', 'JavaScript', 'DSA', 'OOP'
        ],
        'list': ['Python', 'is', 'a', 'programming', 'language'],
        'date': datetime.datetime.now(),
    }
    return render(req, 'navigation/about.html', me)


def contact(req):
    return render(req, 'navigation/contact.html')
