# Generated by Django 4.0.1 on 2022-04-11 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0044_alter_patent_fdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicjournals',
            name='mechanism',
            field=models.CharField(db_column='mechanism', default='无', max_length=20, verbose_name='机构'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 4, 11, 20, 28, 54, 851538), verbose_name='申请日'),
        ),
    ]
