# Generated by Django 4.0.1 on 2022-04-06 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0037_alter_patent_fdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 4, 6, 19, 42, 46, 699760), verbose_name='申请日'),
        ),
    ]
