from rest_framework import serializers
from apps.research.models import Fund, Project, Dynamic


class FundSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','contractamount','arrivalamount','outamount','outsideamount','amount','unit')
        model = Fund


class ProjectSerializers(serializers.ModelSerializer):
    funds = FundSerializers(many=True)

    class Meta:
        fields = "__all__"
        model = Project

    def create(self, validated_data):
        funds = validated_data.pop('funds')
        # validated_data.pop('funds')
        # project = Project.objects.create(projectname=validated_data['projectname'],
        #                                  projecttype=validated_data['projecttype'],
        #                                  projectmember=validated_data['projectmember'],
        #                                  pverify=validated_data['pverify'],
        #                                  ydate=validated_data['ydate'],
        #                                  verify=validated_data['verify'],
        #                                  unit=validated_data['unit'])
        project = Project.objects.create(**validated_data)
        print(funds)
        for funds in funds:
            Fund.objects.create(project=project,**funds)
        return project

    def update(self, instance, validated_data):
        funds = validated_data.pop('funds')
        instance = super().update(instance, validated_data)
        return instance


class DynamicSerializers(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        fields = "__all__"
        model = Dynamic

    def get_projects(self, obj):
        query_set = obj.project
        return [{"projectname": query_set.projectname, "id": query_set.id}]
