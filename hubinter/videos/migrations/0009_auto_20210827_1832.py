# Generated by Django 3.2.2 on 2021-08-27 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='comments_amount',
        ),
        migrations.RemoveField(
            model_name='video',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
    ]
