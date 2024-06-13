from django.shortcuts import render


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
    return render(request, 'index.html', {"data": data})


def about(req, id):
    print(req.GET)
    return render(req, 'index.html', {'id': req.GET})
