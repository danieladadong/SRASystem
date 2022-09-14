from rest_framework import serializers
from apps.customer.models import User
from apps.achievement.models import Academicmonograph, Academicjournals, Achievement, Paper, Patent


# 学术专著
class AcademicmonographSerializers(serializers.ModelSerializer):
    upusers = serializers.SerializerMethodField()
    upuser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        fields = "__all__"
        model = Academicmonograph

    def get_upusers(self, obj):
        query_set = obj.upuser
        return [{"jobno": query_set.jobno, "name": query_set.name}]


# 学术期刊
class AcademicjournalsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Academicjournals


# 科技论文
class PaperSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Paper


# 专利
class PatentSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Patent


# 成果
class AchievementSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Achievement
