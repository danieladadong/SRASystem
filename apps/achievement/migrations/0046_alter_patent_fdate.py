# Generated by Django 4.0.1 on 2022-04-24 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0045_alter_academicjournals_mechanism_alter_patent_fdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 4, 24, 21, 3, 21, 29727), verbose_name='申请日'),
        ),
    ]
