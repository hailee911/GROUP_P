# Generated by Django 5.1.3 on 2024-12-11 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_letter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaryboard',
            name='like_members',
        ),
    ]