from django.http import HttpResponse


def book(request):
    b = (request.POST['code'])
    text = '<h1>Done</h1>'
    return HttpResponse(text)