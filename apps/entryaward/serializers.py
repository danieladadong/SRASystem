from rest_framework import serializers
from apps.entryaward.models import EntryAwards, AchievementAward
from apps.customer.models import User


class EntryAwardsSerializers(serializers.ModelSerializer):
    upusers = serializers.SerializerMethodField()
    upuser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        fields = "__all__"
        model = EntryAwards

    def get_upusers(self, obj):
        query_set = obj.upuser
        return [{"jobno": query_set.jobno, "name": query_set.name}]


class AchievementAwardSerializers(serializers.ModelSerializer):
    upusers = serializers.SerializerMethodField()
    upuser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        fields = "__all__"
        model = AchievementAward

    def get_upusers(self, obj):
        query_set = obj.upuser
        return [{"jobno": query_set.jobno, "name": query_set.name}]
