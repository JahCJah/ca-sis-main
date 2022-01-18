# Generated by Django 3.0.2 on 2022-01-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='s_name',
            new_name='student_firstname',
        ),
        migrations.AddField(
            model_name='student',
            name='student_lastname',
            field=models.CharField(default='testing', max_length=128),
        ),
    ]