# Generated by Django 5.1.3 on 2024-12-11 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_delete_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GroupDiary',
        ),
    ]