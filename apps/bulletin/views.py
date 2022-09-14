import django_filters
from django.shortcuts import render
from django_filters import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import AnnouncementSerializers,AcademicexchangeSerializers
from .models import Announcement,Academicexchange


# Create your views here.

class AnnouncementFilter(django_filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    releaser = filters.CharFilter(lookup_expr="icontains")
    type = filters.CharFilter(lookup_expr="icontains")
    unit = filters.CharFilter(lookup_expr="icontains")
    class Meta:
        models = Announcement
        fields = ('title', 'releaser', 'type','unit')

class AnnouncementModelViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers
    filterset_class = AnnouncementFilter


class AcademicexchangeModelViewSet(ModelViewSet):
    queryset = Academicexchange.objects.all()
    serializer_class = AcademicexchangeSerializers
    filter_fields = ('attendee',)
    # filter_fields = ('exname', 'organizer', 'type', 'cdate', 'verify')

