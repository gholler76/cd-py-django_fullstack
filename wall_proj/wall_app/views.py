from django.shortcuts import HttpResponse, redirect, render
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt


# def index(request):
#     if request.session:
#         print('*****************session id>>>', request.session)
#         return render(request,'board')

#     else:
#         return redirect('/')


def index(request):
    return render(request, 'index.html')


def board(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    messages = Message.objects.all()
    comments = Comment.objects.all()
    context = {
        'name': logged_user.first_name,
        'user_id': logged_user.id,
        'messages': messages,
        'comments': comments
    }
    return render(request, 'board.html', context)


def register(request):
    print(request.POST['password'], request.POST['conf_password'])
    pw_check = request.POST['password'] == request.POST['conf_password']
    if pw_check == False:
        messages.info(request, "Your password entries need to match")
        return redirect('/')
    elif len(request.POST['password']) < 8 or len(request.POST['password']) > 15:
        messages.info(
            request, "Your password must be between 8 and 15 characters")
        return redirect('/')
    else:
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
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
    return redirect('/board')


def logout(request):
    request.session.flush()
    return redirect('/')


def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if len(user_list) == 0:
        messages.info(request, "User email not found")
    else:
        logged_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/board')
        else:
            messages.info(
                request, "Password is incorrect")
            return redirect('/')


def post_message(request):
    user_id = request.session['user_id']
    new_msg = request.POST['post_message']
    print('**********message and user >>>', new_msg, user_id)
    saved_msg = Message.objects.create(
        msg_content=new_msg, posted_by_id=user_id)
    print('**********saved message and user >>>', saved_msg)
    return redirect('/board')


def post_comment(request):
    user_id = request.session['user_id']
    msg = request.POST['message_id']
    new_comment = request.POST['post_comment']
    # print('**********comment message and user >>>', new_msg, user_id)
    saved_comment = Comment.objects.create(
        cmt_content=new_comment, posted_to_id=msg, posted_by_id=user_id)
    # print('**********saved message and user >>>', saved_msg)
    return redirect('/board')


def delete_message(request):
    deleted_msg = request.POST['message.id']
    Message.objects.delete(id=deleted_msg)
    return redirect('/board')
