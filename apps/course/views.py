from django.shortcuts import render, redirect, HttpResponse
from . import models
from .models import Course
# Create your views here.
def index(request):
    courses = models.Course.objects.all()
    context = {
        'courses' : courses
    }
    return render(request, 'course/index.html', context)

def add_course(request):
    post = request.POST
    if post['name'] != '' and post['description'] != '':
        Course.objects.create(name=post['name'], description=post['description'])
    return redirect('/')

def delete_confirm(request, id):
    course = models.Course.objects.filter(id=id)
    context = {
        'course' : course[0]
    }
    return render(request, 'course/delete.html', context)

def delete(request, id):
    models.Course.objects.filter(id=id).delete()
    return redirect('/')
