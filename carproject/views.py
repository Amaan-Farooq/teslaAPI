from django.http import HttpResponse


def handleNull(response):
    response = HttpResponse("This is Home Page")
    return response