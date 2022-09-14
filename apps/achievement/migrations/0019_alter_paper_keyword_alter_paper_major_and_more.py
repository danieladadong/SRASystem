# Generated by Django 4.0.1 on 2022-03-23 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0018_alter_paper_papername_alter_patent_fdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='keyword',
            field=models.CharField(db_column='keyword', max_length=50, verbose_name='关键词'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='major',
            field=models.CharField(db_column='major', max_length=50, verbose_name='学科专业'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 3, 23, 14, 56, 22, 760872), verbose_name='申请日'),
        ),
    ]