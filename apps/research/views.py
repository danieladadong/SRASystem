import django_filters
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FundSerializers, ProjectSerializers, DynamicSerializers
from apps.research.models import Fund, Project, Dynamic
from django_filters import rest_framework as filters


# Create your views here.

class ProjectsFilter(django_filters.FilterSet):
    projectmember = filters.CharFilter(lookup_expr="icontains")
    projectname = filters.CharFilter(lookup_expr="icontains")
    unit = filters.CharFilter(lookup_expr="icontains")
    verify = filters.NumberFilter(lookup_expr="icontains")
    class Meta:
        models = Project
        fields = ('projectmember','projectname','unit',"verify")


class FundModelViewSet(ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializers
    filter_fields = ("unit",'project')


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    filterset_class = ProjectsFilter


class DynamicModelViewSet(ModelViewSet):
    queryset = Dynamic.objects.all()
    serializer_class = DynamicSerializers
    filter_fields = ("unit",)
