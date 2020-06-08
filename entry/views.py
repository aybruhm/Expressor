from django.shortcuts import render, HttpResponseRedirect
from .models import Entry


def home(request):
    posts = Entry.objects.all().order_by('-timestamp')
    return render(request, 'entry/home.html', {'posts': posts})


def add(request):
    if request.method == 'POST':
        if  request.POST.get('author') and request.POST.get('title') and request.POST.get('content'):
            entry = Entry()
            entry.author = request.POST.get('author')
            entry.title = request.POST.get('title')
            entry.content = request.POST.get('content')
            x = entry.save()
            print(x)
            return HttpResponseRedirect('/')
        else:
            pass
    return render(request, 'entry/add.html')


def delete(request, pk):
    print(pk)
    Entry.objects.get(id=pk).delete()
    return HttpResponseRedirect('/')


# def update(request, pk):
#     obj = get_object_or_404(Entry, id=pk)
#     print(obj)
#     form = request.POST.get(
#         'title' or None, instance=obj
#     ) and request.POST.get(
#         'content' or None, instance=obj
#     )
#     print(form)
#     if request.method == 'POST':
#         if form:
#             entry = Entry()
#             entry.title = request.POST.get('title' or None, instance=obj)
#             entry.content = request.POST.get('content' or None, instance=obj)
#             entry.save()
#             return HttpResponseRedirect('/')
#     context = {'form': form, 'obj': obj}
#     return render(request, 'entry/update.html', context)