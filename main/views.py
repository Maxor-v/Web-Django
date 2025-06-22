from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")

def data(request):
    return HttpResponse("<h1>Какие-то ДАННЫЕ</h1>")

def test(request):
    return HttpResponse("<h1>TECT</h1>")