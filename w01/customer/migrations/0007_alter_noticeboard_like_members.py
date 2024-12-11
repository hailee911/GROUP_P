# Generated by Django 5.1.3 on 2024-12-11 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_noticeboard_like_members_and_more'),
        ('loginpage', '0002_alter_member_birthday_alter_member_nicname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='like_members',
            field=models.ManyToManyField(blank=True, related_name='like_noticeboards', to='loginpage.member'),
        ),
    ]
