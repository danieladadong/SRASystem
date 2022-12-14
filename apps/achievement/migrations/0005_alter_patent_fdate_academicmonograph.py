# Generated by Django 4.0.3 on 2022-03-08 09:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('achievement', '0004_academicjournals_alter_patent_fdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='fdate',
            field=models.DateTimeField(db_column='fdate', default=datetime.datetime(2022, 3, 8, 17, 6, 43, 677228), verbose_name='申请日'),
        ),
        migrations.CreateModel(
            name='Academicmonograph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MonographType', models.CharField(db_column='motype', max_length=20, verbose_name='专著类别')),
                ('Monographname', models.CharField(db_column='moname', max_length=20, verbose_name='专著名称')),
                ('author', models.CharField(db_column='author', max_length=20, verbose_name='作者姓名')),
                ('press', models.CharField(db_column='press', max_length=20, verbose_name='出版社')),
                ('upuser', models.ForeignKey(db_column='upuser', on_delete=django.db.models.deletion.CASCADE, to='customer.user', verbose_name='上传用户')),
            ],
            options={
                'db_table': 'acmonograph',
            },
        ),
    ]
