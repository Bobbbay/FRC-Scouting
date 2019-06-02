# Generated by Django 2.2 on 2019-05-11 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0009_auto_20190511_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='match',
            new_name='match_number',
        ),
        migrations.RemoveField(
            model_name='match',
            name='second_start_left',
        ),
        migrations.RemoveField(
            model_name='match',
            name='second_start_right',
        ),
        migrations.RemoveField(
            model_name='team',
            name='second_start_left',
        ),
        migrations.RemoveField(
            model_name='team',
            name='second_start_right',
        ),
        migrations.AddField(
            model_name='match',
            name='first_start',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='match',
            name='second_start',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='team',
            name='first_start',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='team',
            name='second_start',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='team',
            name='matches',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]