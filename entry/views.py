from django.shortcuts import render, HttpResponseRedirect
from .models import Entry


def home(request):
    posts = Entry.objects.all().order_by('-timestamp')
    return render(request, 'entry/home.html', {'posts': posts})


def add(request):
    form = request.POST.get(
        'author'
    ) and request.POST.get(
        'title'
    ) and request.POST.get(
        'content'
    )
    if request.method == 'POST':
        if form:
            entry = Entry()
            entry.author = request.POST.get('author')
            entry.title = request.POST.get('title')
            entry.content = request.POST.get('content')
            x = entry.save()
            print(x)
            return HttpResponseRedirect('/')
        else:
            form
    return render(request, 'entry/add.html')


# def delete(request, pk):
#     print(pk)
#     Entry.objects.get(id=pk).delete()
#     return HttpResponseRedirect('/')