# Generated by Django 4.0.1 on 2022-04-06 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0006_alter_project_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='project',
            field=models.ForeignKey(db_column='project', on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='research.project', verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pverify',
            field=models.IntegerField(db_column='pverify', default=-2, verbose_name='项目状态'),
        ),
    ]
