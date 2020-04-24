from django.http import HttpResponse
from django.shortcuts import render


from . import courses


def courses(request):
    courses = Course.objects.all()

    course_list = "- ".join(courses)
    
