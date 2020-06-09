from django.shortcuts import render, HttpResponseRedirect
from .models import Entry
from .forms import EntryForm


def home(request):
    posts = Entry.objects.all().order_by('-timestamp')
    return render(request, 'entry/home.html', {'posts': posts})


def add(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'entry/add.html', {'form': form})


def delete(request, pk):
    print(pk)
    Entry.objects.get(id=pk).delete()
    return HttpResponseRedirect('/')


def update(request, pk):
    entry = Entry.objects.get(id=pk)
    form = EntryForm(instance=entry)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'entry/update.html', {'form': form})