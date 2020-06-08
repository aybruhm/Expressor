from django.shortcuts import render, HttpResponse
from .models import Entry


def home(request):
    posts = Entry.objects.all().order_by('-timestamp')
    return render(request, 'entry/home.html', {'posts': posts})


def add(request):
    pass

def delete(request):
    pass