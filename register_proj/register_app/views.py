from django.shortcuts import HttpResponse, redirect, render
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return redirect(hello)


def hello(request):
    return render(request, 'hello.html')


def register(request):
    print(request.POST['password'], request.POST['conf_password'])
    context = {
        'first_name': request.POST['first_name']
    }
    pw_check = request.POST['password'] == request.POST['conf_password']
    if pw_check == False:
        messages.info(request, "Your password entries need to match")
        return redirect(hello)
    elif len(request.POST['password']) < 8 or len(request.POST['password']) > 15:
        messages.info(
            request, "Your password must be between 8 and 15 characters")
        return redirect(hello)
    else:
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/hello')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()).decode()
            print('**********pwhash >>>', pw_hash)

            logged_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )
            request.session['user_id'] = logged_user.id
            print(logged_user.id)
    return redirect(success)


def success(request):
    if request.session['user_id']:
        print('************user session >>>', request.session['user_id'])
        logged_user = User.objects.get(id=request.session['user_id'])
        context = {
            'name': logged_user.first_name,
        }
        return render(request, 'success.html', context)
    else:
        return redirect('/')


def logout(request):
    request.session.flush()
    # if request.session['user_id']:
    #     request.session['user_id'].flush()
    #     return redirect('/')
    # else:
    return redirect('/')


def login(request):
    user = User.objects.get(email=request.POST['email'])
    if user:
        logged_user = user
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect(success)
        else:
            messages.info(
                request, "Password is incorrect")
    else:
        messages.info(
            request, "User email not found")
    return redirect('/')
