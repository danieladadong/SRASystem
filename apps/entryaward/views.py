from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from apps.entryaward.models import EntryAwards,AchievementAward


# Create your views here.

class EntryAwardsModelViewSet(ModelViewSet):
    queryset = EntryAwards.objects.all()
    serializer_class = EntryAwardsSerializers
    filter_fields = ("awardType", "upuser", "awarding","verify","unit")


class AchievementAwardModelViewSet(ModelViewSet):
    queryset = AchievementAward.objects.all();
    serializer_class = AchievementAwardSerializers
    filter_fields = ("awardType", "upuser", "awarding", "verify","unit")

