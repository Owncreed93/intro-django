from django.http import HttpResponse


def hell_world(request):

    return HttpResponse('Hola Mundo')