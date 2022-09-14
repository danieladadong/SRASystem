import json
import time

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from apps.achievement.models import Patent, Paper, Achievement, Academicjournals
from .spiders import Spiders


# Create your views here.
class JournalsView(View):

    @csrf_exempt
    def post(self, request):
        tag = request.POST.get("tag")
        author = request.POST.get("author")
        school = request.POST.get("school")
        unit = request.POST.get("unit")
        if tag == 'onepunch':
            patents = Patent.objects.filter(isadd=0,inventor__icontains=author)
            patents.delete()
            papers = Paper.objects.filter(isadd=0,author__icontains=author)
            papers.delete()
            achievements = Achievement.objects.filter(isadd=0,completed__icontains=author)
            achievements.delete()
            acjournals = Academicjournals.objects.filter(isadd=0,author__icontains=author)
            acjournals.delete()
            tag = "专利"
            Spiders.SearchPatent(Spiders, tag, 发明人=author, anvalue=school,unit=unit)
            time.sleep(3)
            tag = "成果"
            Spiders.SearchAchievement(Spiders, tag, 成果完成人=author, anvalue=school,unit=unit)
            time.sleep(3)
            tag = "学术期刊"
            Spiders.SearchThing(Spiders, tag, 作者=author, ankey="作者单位", anvalue=school,unit=unit)
            time.sleep(3)
            tag = "学位论文"
            Spiders.SearchThing(Spiders, tag, 作者=author, ankey="", anvalue="",unit=unit)
            data = {
                "status": 200,
                "success": True,
                "message": "一键同步成功！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            if tag == "专利":
                Spiders.SearchPatent(Spiders,tag,发明人=author,anvalue=school,unit=unit)
            elif tag == "成果":
                Spiders.SearchAchievement(Spiders,tag, 成果完成人=author, anvalue=school,unit=unit)
            elif tag == "学术期刊":
                Spiders.SearchThing(Spiders,tag,作者=author,ankey="作者单位",anvalue=school,unit=unit)
            elif tag == "学位论文":
                Spiders.SearchThing(Spiders,tag,作者=author,ankey="",anvalue="",unit=unit)
            data = {
                "status": 200,
                "success": True,
                "message": "同步成功！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')

