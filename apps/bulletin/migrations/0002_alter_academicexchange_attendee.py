# Generated by Django 4.0.1 on 2022-03-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('bulletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicexchange',
            name='attendee',
            field=models.ManyToManyField(db_column='attendee', to='customer.User', verbose_name='参会人'),
        ),
    ]
