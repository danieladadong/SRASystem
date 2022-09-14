from django.db import models
from apps.customer.models import User


# Create your models here.

# 专业参赛奖项
class EntryAwards(models.Model):
    awardType = models.CharField(verbose_name="奖项类型", db_column="awardtype", max_length=20)
    title = models.CharField(verbose_name="奖项名称", db_column="title", max_length=20)
    winner = models.CharField(verbose_name="得奖人", db_column="winner", max_length=40)
    awarding = models.CharField(verbose_name="颁奖机构", db_column="awarding", max_length=35)
    certificate = models.CharField(verbose_name="证书名", db_column="certificate", max_length=50)
    upuser = models.ForeignKey(User, verbose_name="上传用户", db_column="upuser", on_delete=models.CASCADE)
    verify = models.IntegerField(verbose_name="审核状态", db_column="verify", default=-1)
    unit = models.CharField(verbose_name="单位", db_column="unit", max_length=30)

    class Meta:
        db_table = "entryawards"


# 成果奖项
class AchievementAward(models.Model):
    awardType = models.CharField(verbose_name="奖项类型", db_column="awardtype", max_length=20)
    title = models.CharField(verbose_name="奖项名称", db_column="title", max_length=20)
    winner = models.CharField(verbose_name="得奖人", db_column="winner", max_length=40)
    awarding = models.CharField(verbose_name="颁奖机构", db_column="awarding", max_length=35)
    certificate = models.CharField(verbose_name="证书", db_column="certificate", max_length=50)
    upuser = models.ForeignKey(User, verbose_name="上传用户", db_column="upuser", on_delete=models.CASCADE)
    verify = models.IntegerField(verbose_name="审核状态", db_column="verify", default=-1)
    unit = models.CharField(verbose_name="单位", db_column="unit", max_length=30)

    class Meta:
        db_table = "acaward"
