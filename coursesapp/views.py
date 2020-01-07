

from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
from coursesapp.models import Courses
from coursesapp.models import Portfolio


def index(request):

    courses=Courses.objects.all()

    pf=Portfolio.objects.all()


    return render(request,"index.html",{'courses':courses,'pf':pf})








