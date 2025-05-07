from django.http import HttpResponse


def book(request):
    b = (request.POST['code'])
    b = request.readline
    print(b)
    text = '<h1>Done</h1>'
    return HttpResponse(text)