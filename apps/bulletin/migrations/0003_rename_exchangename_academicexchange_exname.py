# Generated by Django 4.0.1 on 2022-04-06 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0002_alter_academicexchange_attendee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicexchange',
            old_name='exchangename',
            new_name='exname',
        ),
    ]
