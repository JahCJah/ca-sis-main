# Generated by Django 3.0.2 on 2022-01-15 06:09

import django.core.validators
from django.db import migrations, models
import sis_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0002_auto_20220115_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='enrollment_status',
            field=models.CharField(choices=[('Not Enrolled', 'Not Enrolled'), ('Enrolled', 'Enrolled')], default='Not Enrolled', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='student_schoolyear_start',
            field=models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(2000), sis_app.models.max_value_current_year], verbose_name='year'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_lastname',
            field=models.CharField(max_length=128),
        ),
    ]
