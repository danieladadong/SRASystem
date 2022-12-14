# Generated by Django 4.0.1 on 2022-04-07 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0041_alter_patent_fdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicjournals',
            name='isadd',
            field=models.IntegerField(db_column='isadd', default=0, verbose_name='是否为添加'),
        ),
        migrations.AddField(
            model_name='academicmonograph',
            name='isadd',
            field=models.IntegerField(db_column='isadd', default=0, verbose_name='是否为添加'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='isadd',
            field=models.IntegerField(db_column='isadd', default=0, verbose_name='是否为添加'),
        ),
        migrations.AddField(
            model_name='paper',
            name='isadd',
            field=models.IntegerField(db_column='isadd', default=0, verbose_name='是否为添加'),
        ),
        migrations.AddField(
            model_name='patent',
            name='isadd',
            field=models.IntegerField(db_column='isadd', default=0, verbose_name='是否为添加'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 4, 7, 20, 44, 59, 942709), verbose_name='申请日'),
        ),
    ]
