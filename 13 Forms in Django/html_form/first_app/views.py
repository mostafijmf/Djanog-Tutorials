from django.shortcuts import render
from . forms import contactForm, StudentData, PasswordValidationProject


def index(request):
    data = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "email": "Sincere@april.biz",
            "phone": "1-770-736-8031 x56442",
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "email": "Shanna@melissa.tv",
            "phone": "010-692-6593 x09125",
        },
        {
            "id": 3,
            "name": "Clementine Bauch",
            "email": "Nathan@yesenia.net",
            "phone": "1-463-123-4447",
        },
        {
            "id": 4,
            "name": "Patricia Lebsack",
            "email": "Julianne.OConner@kory.org",
            "phone": "493-170-9623 x156",
        },
        {
            "id": 5,
            "name": "Chelsey Dietrich",
            "email": "Lucio_Hettinger@annie.ca",
            "phone": "(254)954-1289",
        }
    ]
    return render(request, 'about.html', {"data": data})


def about(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        select = req.POST.get('select')
        return render(req, 'about.html', {'name': name, 'email': email, 'select': select})
    return render(req, 'about.html')


def submit_form(req):
    print(req)
    return render(req, 'form.html')


def DjangoForm(req):
    if req.method == 'POST':
        form = contactForm(req.POST, req.FILES)
        if form.is_valid():
            #     file = form.cleaned_data['file']
            #     with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #         for chunk in file.chunks():
            #             destination.write(chunk)
            print(form.cleaned_data)
        return render(req, 'django_form.html', {'form': form})
    else:
        form = contactForm()
    return render(req, 'django_form.html', {'form': form})


def StudentForm(req):
    if req.method == 'POST':
        form = StudentData(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(req, 'django_form.html', {'form': form})

def PasswordValidation(req):
    if req.method == 'POST':
        form = PasswordValidationProject(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(req, 'django_form.html', {'form': form})
