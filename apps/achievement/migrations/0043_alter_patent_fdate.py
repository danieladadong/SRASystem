# Generated by Django 4.0.1 on 2022-04-08 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0042_academicjournals_isadd_academicmonograph_isadd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 4, 8, 19, 5, 41, 100162), verbose_name='申请日'),
        ),
    ]