# Generated by Django 2.2 on 2019-05-28 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0027_schedule_played'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start',
        ),
    ]