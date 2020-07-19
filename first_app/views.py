from django.http import HttpResponse
from django.shortcuts import render
import datetime
import os
from django.urls import reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время':  reverse('time'),
        'Показать содержимое рабочей директории':  reverse('workdir'),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    now = datetime.datetime.now()
    msg = f'Текущее время: {now}'
    return HttpResponse(msg)


def workdir_view(request):
    dir_list = []
    work_dir = os.listdir('first_project')
    dir_list.append(work_dir)
    return HttpResponse(dir_list)
