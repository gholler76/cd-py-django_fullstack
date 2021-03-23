from django.shortcuts import HttpResponse, redirect, render
from .models import Show


def index(request):
    return redirect('/shows')


def shows_new(request):
    return render(request, 'shows/new.html')


def shows(request):
    shows = Show.objects.all()

    context = {
        "shows": shows
    }
    return render(request, 'shows.html', context)


def shows_info(request, num):
    show = Show.objects.get(id=num)

    context = {
        "show": show
    }
    return render(request, 'info.html', context)


def shows_edit(request, num):
    show = Show.objects.get(id=num)

    context = {
        "show": show
    }
    return render(request, 'edit.html', context)


def shows_update(request, num):
    Show.objects.filter(id=num).update(
        title=request.POST['title'],
        network=request.POST['network'],
        date=request.POST['date'],
        desc=request.POST['desc']
    )

    return redirect(shows_info, num)


def shows_create(request):
    new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        date=request.POST['date'],
        desc=request.POST['desc']
    )
    num = new_show.id

    return redirect(shows_info, num)


def shows_destroy(request, num):
    Show.objects.filter(id=num).delete()
    return redirect("/shows")
