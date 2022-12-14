# Generated by Django 4.0.3 on 2022-03-08 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryAwards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awardType', models.CharField(db_column='awardtype', max_length=20, verbose_name='奖项类型')),
                ('title', models.CharField(db_column='title', max_length=20, verbose_name='奖项名称')),
                ('awarding', models.CharField(db_column='awarding', max_length=35, verbose_name='颁奖机构')),
                ('certificate', models.CharField(db_column='certificate', max_length=50, verbose_name='证书名')),
                ('upuser', models.CharField(db_column='upuser', max_length=40, verbose_name='上传用户')),
                ('verify', models.IntegerField(db_column='verify', default=-1, verbose_name='审核状态')),
                ('winner', models.ForeignKey(db_column='winner', on_delete=django.db.models.deletion.CASCADE, to='customer.user', verbose_name='得奖人')),
            ],
            options={
                'db_table': 'entryawards',
            },
        ),
        migrations.CreateModel(
            name='AchievementAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awardType', models.CharField(db_column='awardtype', max_length=20, verbose_name='奖项类型')),
                ('title', models.CharField(db_column='title', max_length=20, verbose_name='奖项名称')),
                ('awarding', models.CharField(db_column='awarding', max_length=35, verbose_name='颁奖机构')),
                ('certificate', models.CharField(db_column='certificate', max_length=50, verbose_name='证书')),
                ('upuser', models.CharField(db_column='upuser', max_length=40, verbose_name='上传用户')),
                ('verify', models.IntegerField(db_column='verify', default=-1, verbose_name='审核状态')),
                ('winner', models.ForeignKey(db_column='winner', on_delete=django.db.models.deletion.CASCADE, to='customer.user', verbose_name='得奖人')),
            ],
            options={
                'db_table': 'acaward',
            },
        ),
    ]
