from django.db import models


# Create your models here.
##登录用
class User(models.Model):
    jobno = models.IntegerField(primary_key=True, verbose_name="工号", db_column="jobno")
    name = models.CharField(verbose_name="姓名", db_column="name", max_length=20)
    pwd = models.CharField(verbose_name="密码", db_column="pwd", max_length=30)
    teatype = models.IntegerField(verbose_name="类别", db_column="teatype", default=0)
    unit = models.CharField(verbose_name="单位名称", db_column="unit", max_length=40)

    class Meta:
        db_table = "user"
        verbose_name_plural = "用户管理"


##个人信息表
class Profile(models.Model):
    name = models.CharField(verbose_name="姓名", db_column="name", max_length=20)
    sex = models.CharField(verbose_name="性别", db_column="sex", default="男", max_length=4)
    brith = models.CharField(verbose_name="出生日期", db_column="brith", max_length=15)
    mail = models.EmailField(verbose_name="邮箱", db_column="mail", max_length=20)
    phone = models.CharField(verbose_name="联系方式", db_column="phone", max_length=12)
    access = models.CharField(verbose_name="地址", db_column="access", max_length=50)
    position = models.CharField(verbose_name="职位", db_column="position", max_length=15)
    education = models.CharField(verbose_name="学历", db_column="education", max_length=10)
    unit = models.CharField(verbose_name="单位名称", db_column="unit", max_length=40)

    class Meta:
        db_table = "profile"

