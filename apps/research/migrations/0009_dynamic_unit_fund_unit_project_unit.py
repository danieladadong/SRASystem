# Generated by Django 4.0.1 on 2022-04-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0008_alter_fund_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamic',
            name='unit',
            field=models.CharField(db_column='unit', default='山东女子学院', max_length=30, verbose_name='单位'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fund',
            name='unit',
            field=models.CharField(db_column='unit', default='山东女子学院', max_length=30, verbose_name='单位'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='unit',
            field=models.CharField(db_column='unit', default='山东女子学院', max_length=30, verbose_name='单位'),
            preserve_default=False,
        ),
    ]