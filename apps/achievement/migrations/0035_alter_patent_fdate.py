# Generated by Django 4.0.1 on 2022-04-06 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0034_alter_patent_fdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 4, 6, 15, 19, 11, 717735), verbose_name='申请日'),
        ),
    ]
