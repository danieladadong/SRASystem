from django.db import models


# Create your models here.


# 项目
class Project(models.Model):
    projectname = models.CharField(verbose_name="项目名称", db_column="projectname", max_length=20)
    projecttype = models.CharField(verbose_name="项目分类", db_column="projecttype", max_length=20)
    projectmember = models.CharField(verbose_name="项目成员", db_column="projectmember", max_length=20)
    pverify = models.IntegerField(verbose_name="项目状态", db_column="pverify", default=-2)
    ydate = models.CharField(verbose_name="起止时间", db_column="ydate", max_length=20)
    verify = models.IntegerField(verbose_name="审核状态", db_column="verify", default=-1)
    unit = models.CharField(verbose_name="单位", db_column="unit", max_length=30)

    class Meta:
        db_table = "project"


# 经费
class Fund(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目名称", db_column="project", on_delete=models.CASCADE, related_name="funds")
    contractamount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="合同金额", db_column="comount")
    arrivalamount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="到账金额", db_column="arrmount")
    outamount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="支出金额", db_column="outamount")
    outsideamount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="外拨金额", db_column="outmount")
    amount = models.TextField(verbose_name="经费明细", db_column="amount")
    unit = models.CharField(verbose_name="单位", db_column="unit", max_length=30)

    class Meta:
        db_table = "fund"


# 科研动态

class Dynamic(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目名称", db_column="project", on_delete=models.CASCADE)
    progress = models.CharField(verbose_name="项目进度", db_column="progress", max_length=20)
    performance = models.CharField(verbose_name="完成进度", db_column="performance", max_length=20)
    ddate = models.CharField(verbose_name="当前时间", db_column="ddate", max_length=20)
    unit = models.CharField(verbose_name="单位", db_column="unit", max_length=30)

    class Meta:
        db_table = "dynamic"
