from django.db import models
from apps.customer.models import User


# Create your models here.


# 公告信息
class Announcement(models.Model):
    title = models.CharField(verbose_name="标题", db_column="title", max_length=20)
    releasedate = models.CharField(verbose_name="发布时间", db_column="release", max_length=20)
    releaser = models.ForeignKey(User, verbose_name="发布人", db_column="releaser", on_delete=models.CASCADE)
    content = models.CharField(verbose_name="内容", db_column="content", max_length=20)
    type = models.CharField(verbose_name="类型", db_column="type", max_length=20)
    unit = models.CharField(verbose_name="单位",db_column="unit",max_length=30)

    class Meta:
        db_table = "anment"


# 学术交流
class Academicexchange(models.Model):
    exname = models.CharField(verbose_name="会议名称", db_column="exname", max_length=20)
    attendee = models.ManyToManyField(User)
    organizer = models.CharField(verbose_name="主办单位", db_column="organizer", max_length=20)
    type = models.CharField(verbose_name="会议类型", db_column="type", max_length=20)
    cdate = models.CharField(verbose_name="参会日期", db_column="cdate", max_length=20)
    verify = models.IntegerField(verbose_name="审核状态", db_column="verify", default=-1)
    unit = models.CharField(verbose_name="单位", db_column="unit", max_length=30)

    class Meta:
        db_table = "acexchange"
