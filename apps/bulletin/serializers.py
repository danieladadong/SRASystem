from rest_framework import serializers
from apps.customer.models import User
from .models import Announcement, Academicexchange


class AnnouncementSerializers(serializers.ModelSerializer):
    releasers = serializers.SerializerMethodField()
    releaser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        fields = "__all__"
        model = Announcement

    def get_releasers(self, obj):
        query_set = obj.releaser
        return [{"jobno": query_set.jobno, "name": query_set.name}]


class AcademicexchangeSerializers(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Academicexchange


