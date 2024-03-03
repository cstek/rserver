from django.shortcuts import render
from datetime import datetime
import geocoder
import requests
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from rser.models import User, Tag, Log


def home(request):
    template = loader.get_template('index.html')
    msg = 'this is test home message'
    context = {'msg': msg}
    return HttpResponse(template.render(context, request))


def createUser(request):
    user = User.objects.create_user('username', 'email@xx.com', 'password')
    user.save()
    return HttpResponse("user created ")


def createTag(request):
    tag = Tag(tag_id='12345', tag_status='active')
    tag.save()
    return HttpResponse("Tag created")


def attachUserToTag(request, user_id, tag_id):
    user = User.objects.get(user_id=user_id)
    tag = Tag.objects.get(tag_id=tag_id)
    tag.user = user
    tag.save()
    return HttpResponse("attached tag to user")


def createLog(user, tag, event):
    log = Log(user=user, tag=tag, time=timezone.now(), event=event)
    log.save()
    return HttpResponse("log created")


def testMsg(request):
    return HttpResponse("TEST MESSAGE")