import json

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .serializers import UserSerializers,ProfileSerializers
from apps.customer.models import User,Profile
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_fields = ('jobno','name')

class LoginView(View):
    def get(self,request):
        pass

    def post(self,request):
        jobnos = request.POST.get("jobno")
        pwds = request.POST.get("pwd")
        print(jobnos)
        user = User.objects.get(jobno=jobnos)
        if user:
            if user.pwd.__eq__(pwds):
                data = {
                    "status": 200,
                    "success": True,
                    "teatype":user.teatype,
                    "unit":user.unit,
                    "message": "登录成功！",
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {
                    "status": 400,
                    "success": False,
                    "message": "用户名或密码错误！"
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                "status": 400,
                "success": False,
                "message": "用户不存在，请先注册！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')

class RegistView(View):
    def post(self,request):
        jobno = request.POST.get('jobno')
        pwd = request.POST.get('pwd')
        name = request.POST.get("name")
        teatype = request.POST.get("teatype")
        unit = request.POST.get("unit")
        print(pwd)
        same_user = User.objects.filter(name=name)
        if same_user:
            data = {
                "status": 400,
                "success": False,
                "message": "账号已存在！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            user = User.objects.create(jobno=jobno, name=name, pwd=pwd, teatype=teatype, unit=unit)
            user.save()
            profile = Profile.objects.create(id=jobno, name=name,unit=unit)
            profile.save()
            data = {
                "status": 200,
                "success": True,
                "message": "创建成功！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class ProfileModelViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    filter_fields = ('id','name','position','education','phone','unit')

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_fields = ('unit',)