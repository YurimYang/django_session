# Generated by Django 3.1.2 on 2021-05-23 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210523_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='writer',
        ),
    ]