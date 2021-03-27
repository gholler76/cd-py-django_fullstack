from django.shortcuts import HttpResponse, redirect, render
from .models import Show
from django.contrib import messages


def index(request):
    return redirect('/shows')


def shows_new(request):
    return render(request, 'new.html')


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
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(shows_edit, num)

    else:

        Show.objects.filter(id=num).update(
            title=request.POST['title'],
            network=request.POST['network'],
            date=request.POST['date'],
            desc=request.POST['desc'])
        messages.success(request, "Show updated successfully")

    return redirect(shows_info, num)


def shows_create(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/shows/new')

    else:
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
