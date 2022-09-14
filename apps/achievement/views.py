import json

import django_filters
from django.db.models import Count
from django.db.models.functions import TruncYear, ExtractYear
from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.core import serializers as se
from apps.achievement.models import *
from django_filters import rest_framework as filters


# Create your views here.

class AcMonographFilter(django_filters.FilterSet):
    author = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        models = Academicmonograph
        fields = 'author'


class AcmonographModelViewSet(ModelViewSet):
    queryset = Academicmonograph.objects.all()
    serializer_class = AcademicmonographSerializers
    # filter_fields = ('author', 'press')
    filterset_class = AcMonographFilter


class AcjournalsFilter(django_filters.FilterSet):
    author = filters.CharFilter(lookup_expr="icontains")
    mechanism = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        models = Academicjournals
        fields = ('author', 'mechanism')


class AcjournalsModelViewSet(ModelViewSet):
    queryset = Academicjournals.objects.all()
    serializer_class = AcademicjournalsSerializers
    # filter_fields = ('author', 'mechanism')
    filterset_class = AcjournalsFilter


class PaperFilter(django_filters.FilterSet):
    papername = filters.CharFilter(lookup_expr="icontains")
    author = filters.CharFilter(lookup_expr="icontains")
    school = filters.CharFilter(lookup_expr="icontains")


class PaperModelViewSet(ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializers
    # filter_fields = ('papername', 'author', 'school')
    filterset_class = PaperFilter


class PatentFilter(django_filters.FilterSet):
    inventor = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        models = Patent
        fields = 'inventor'


class PatentModelViewSet(ModelViewSet):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializers
    # filter_fields = ('patename', 'patenttype', 'applicant', 'inventor', 'fdate')
    filterset_class = PatentFilter


class AchievementFilter(django_filters.FilterSet):
    completed = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        models = Achievement
        fields = 'completed'


class AchievementModelViewSet(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializers
    # filter_fields = ('completed', 'first', 'ydate', 'actype')
    filterset_class = AchievementFilter


class AchievementStatistics(View):

    def post(self, request):
        params = request.POST.get('params')
        author = request.POST.get('author')
        unit = request.POST.get('unit')
        if params == 'category':
            num = Achievement.objects.values('achievementype','ydate').annotate(total=Count('id')).filter(completed__contains=author).filter(unit__contains=unit)
        elif params == 'ydate':
            num = Achievement.objects.values('ydate').annotate(total=Count('id')).filter(completed__contains=author).filter(unit__contains=unit)
        elif params == 'unit':
            num = Achievement.objects.values('unit').annotate(total=Count('id'))
        return HttpResponse(json.dumps(list(num)), content_type='application/json')

    def get(self, request):
        pass

class PatentStatistics(View):
    def post(self,request):
        params = request.POST.get('params')
        author = request.POST.get('author')
        unit = request.POST.get('unit')
        if params == 'fdate':
            num = Patent.objects.annotate(year=ExtractYear('fdate')).values('year').annotate(total=Count('id')).filter(inventor__contains=author).filter(unit__contains=unit)
        elif params == 'special':
            num = Patent.objects.values('special').annotate(total=Count('id')).filter(inventor__contains=author).filter(unit__contains=unit)
        elif params == 'patenttype':
            num = Patent.objects.values('patenttype').annotate(total=Count('id')).filter(inventor__contains=author).filter(unit__contains=unit)
        elif params == 'unit':
            num = Patent.objects.values('unit').annotate(total=Count('id'))
        return HttpResponse(json.dumps(list(num)), content_type='application/json')
    def get(self,request):
        pass

class PaperStatistics(View):
    def post(self,request):
        params = request.POST.get('params')
        author = request.POST.get('author')
        unit = request.POST.get('unit')
        if params == 'school':
            num = Paper.objects.values('school').annotate(total=Count('id')).filter(author__contains=author).filter(unit__contains=unit)
        elif params == 'major':
            num = Paper.objects.values('major').annotate(total=Count('id')).filter(author__contains=author).filter(unit__contains=unit)
        elif params == 'unit':
            num = Paper.objects.values('unit').annotate(total=Count('id'))
        elif params == 'fdate':
            num = Paper.objects.values('fdate').annotate(
                total=Count('id')).filter(author__contains=author).filter(unit__contains=unit)
        return HttpResponse(json.dumps(list(num)), content_type='application/json')
    def get(self,request):
        pass

class AjStatistics(View):
    def post(self,request):
        params = request.POST.get('params')
        author = request.POST.get('author')
        unit = request.POST.get('unit')
        if params == 'mechanism':
            num = Academicjournals.objects.values('mechanism').annotate(total=Count('id')).filter(author__contains=author)
        elif params == 'unit':
            num = Academicjournals.objects.values('unit').annotate(total=Count('id'))
        elif params == 'fdate':
            num = Academicjournals.objects.annotate(year=ExtractYear('fdate')).values('year').annotate(
                total=Count('id')).filter(author__contains=author).filter(unit__contains=unit)
        return HttpResponse(json.dumps(list(num)), content_type='application/json')
    def get(self,request):
        pass
