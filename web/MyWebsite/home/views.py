from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home import models
from django.shortcuts import redirect
import re
import time
import json

# 注册
def registered(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    models.UserTable.objects.create(
        username=username,password=password,user_id=username,creat_date=int(time.time()),update_date=int(time.time()))
    return render(request,'注册成功')


#登录
def user_login(request):
    if request.method =="GET":
        return render(request)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        md = models.UserTable.objects.filter(username=username,password=password)
        if md:
            return HttpResponse(request,'登录成功！')
        else:
            return HttpResponse(request,'用户名或密码错误！')

#添加留言
def message(request):
    msg = request.POST.get('msg')
    models.LeaveMessage.objects.create(message=msg,create_date=int(time.time()))
    return render(request,'恭喜你啊')
