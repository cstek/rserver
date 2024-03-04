from django.contrib import messages
from django.shortcuts import render
from datetime import datetime
import geocoder
import requests
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rser.models import User, Tag, Log


def home(request):
    template = loader.get_template('index.html')
    msg = 'this is test home message'
    if request.user.is_authenticated:
        # 获取当前登录用户关联的所有标签的tag_id列表
        tag_ids = Tag.objects.filter(user=request.user).values_list('tag_id', flat=True)
    else:
        tag_ids = []
    context = {'msg': msg,
               'tag_ids': tag_ids,
               }
    return HttpResponse(template.render(context, request))


def logIn(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'login.html')


def logOut(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        user_id = request.POST['user_id']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # 确保两次输入的密码匹配
        if password == password2:
            # 创建新用户
            user = User.objects.create_user(user_id=user_id, username=username, password=password)
            user.save()

            # 可选：登录新用户并重定向到首页
            login(request, user)
            return redirect('home')  # 确保你有一个名为'home'的URL pattern
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'register.html')


def attach(request):
    if request.method == "GET":
        return render(request, 'attach.html')
    elif request.method == "POST":
        tag_id = request.POST['tag_id']
        user = request.user
        tag = Tag(tag_id=tag_id, tag_status='active')
        tag.user = user
        tag.save()
        return redirect('home')


def createLog(user, tag, event):
    log = Log(user=user, tag=tag, time=timezone.now(), event=event)
    log.save()
    return HttpResponse("log created")


def testMsg(request):
    return HttpResponse("TEST MESSAGE")