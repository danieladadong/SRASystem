# Generated by Django 4.0.1 on 2022-03-22 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0016_alter_academicjournals_journalsname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicjournals',
            name='keyword',
            field=models.CharField(db_column='keyword', max_length=50, verbose_name='关键词'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 3, 22, 21, 56, 1, 101239), verbose_name='申请日'),
        ),
    ]