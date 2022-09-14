import django_filters
from django.db import models
from apps.customer.models import User
import datetime


# Create your models here.


# 学术专著
class Academicmonograph(models.Model):
    MonographType = models.CharField(verbose_name="专著类别", db_column="motype", max_length=20)
    Monographname = models.CharField(verbose_name="专著名称", db_column="moname", max_length=20)
    author = models.CharField(verbose_name="作者姓名", db_column="author", max_length=20)
    press = models.CharField(verbose_name="出版社", db_column="press", max_length=20)
    upuser = models.ForeignKey(User, verbose_name="上传用户", db_column="upuser", on_delete=models.CASCADE)
    isadd = models.IntegerField(verbose_name="是否为添加",db_column="isadd",default=0)
    unit = models.CharField(verbose_name="所属学院",db_column="unit",max_length=50,default=None)

    class Meta:
        db_table = "acmonograph"


# 以下为爬取内容，不设外键

# 学术期刊
class Academicjournals(models.Model):
    journalsname = models.CharField(verbose_name="标题", db_column="joname", max_length=50)
    author = models.CharField(verbose_name="作者", db_column="author", max_length=20)
    mechanism = models.CharField(verbose_name="机构", db_column="mechanism", max_length=20,default="无")
    abstract = models.TextField(verbose_name="摘要", db_column="abstract")
    keyword = models.CharField(verbose_name="关键词", db_column="keyword", max_length=50)
    content = models.TextField(verbose_name="详情", db_column="content")
    isadd = models.IntegerField(verbose_name="是否为添加", db_column="isadd", default=0)
    unit = models.CharField(verbose_name="所属学院", db_column="unit",max_length=50, default=None)
    fdate = models.DateTimeField(verbose_name="发表日期", db_column="fdate", default=datetime.datetime.now())

    class Meta:
        db_table = "acjournals"


# 科技论文
class Paper(models.Model):
    papername = models.TextField(verbose_name="标题", db_column="papername")
    author = models.CharField(verbose_name="作者", db_column="author", max_length=60)
    school = models.CharField(verbose_name="学校", db_column="school", max_length=60)
    abstract = models.TextField(verbose_name="摘要", db_column="abstract")
    keyword = models.TextField(verbose_name="关键词", db_column="keyword")
    tteacher = models.CharField(verbose_name="导师", db_column="tteacher", max_length=60)
    major = models.CharField(verbose_name="学科专业", db_column="major", max_length=50)
    content = models.TextField(verbose_name="详情", db_column="content")
    isadd = models.IntegerField(verbose_name="是否为添加", db_column="isadd", default=0)
    unit = models.CharField(verbose_name="所属学院", db_column="unit",max_length=50, default=None)
    fdate = models.CharField(verbose_name="发表日期", db_column="fdate", max_length=30,default="")

    class Meta:
        db_table = "paper"


# 专利
class Patent(models.Model):
    patentname = models.CharField(verbose_name="专利名", db_column="patename", max_length=20)
    patenttype = models.CharField(verbose_name="专利类型", db_column="patenttype", max_length=50)
    applicant = models.CharField(verbose_name="申请人", db_column="applicant", max_length=50)
    address = models.TextField(verbose_name="地址", db_column="address")
    inventor = models.CharField(verbose_name="发明人", db_column="inventor", max_length=50)
    special = models.CharField(verbose_name="专题", db_column="special", max_length=20)
    album = models.CharField(verbose_name="专辑", db_column="album", max_length=50)
    pages = models.IntegerField(verbose_name="页数", db_column="pages")
    agency = models.TextField(verbose_name="代理机构", db_column="agency")
    fdate = models.DateTimeField(verbose_name="申请日", db_column="fdate", default=datetime.datetime.now())
    abstract = models.TextField(verbose_name="摘要", db_column="abstract")
    isadd = models.IntegerField(verbose_name="是否为添加", db_column="isadd", default=0)
    unit = models.CharField(verbose_name="所属学院", db_column="unit",max_length=50, default=None)

    class Meta:
        db_table = "patent"


# 成果
class Achievement(models.Model):
    title = models.TextField(verbose_name="标题",db_column="title")
    completed = models.TextField(verbose_name="成果完成人", db_column="completed")
    first = models.CharField(verbose_name="第一完成单位", db_column="first", max_length=40)
    keyword = models.TextField(verbose_name="关键词", db_column="keyword")
    introduction = models.TextField(verbose_name="成果简介", db_column="induction")
    achievementype = models.CharField(verbose_name="成果类别", db_column="actype", max_length=30)
    ydate = models.TextField(verbose_name="研究起止时间", db_column="ydate")
    isadd = models.IntegerField(verbose_name="是否为添加", db_column="isadd", default=0)
    unit = models.CharField(verbose_name="所属学院", db_column="unit",max_length=50, default=None)


    class Meta:
        db_table = "achievement"

