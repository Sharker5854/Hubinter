# Generated by Django 3.2.2 on 2021-06-28 12:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='disliked_videos',
            field=models.ManyToManyField(related_name='disliked_by', to='videos.Video', verbose_name='Disliked videos'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_videos',
            field=models.ManyToManyField(related_name='liked_by', to='videos.Video', verbose_name='Liked videos'),
        ),
        migrations.AddField(
            model_name='user',
            name='notifications',
            field=models.ManyToManyField(related_name='_accounts_user_notifications_+', to=settings.AUTH_USER_MODEL, verbose_name='Notifications'),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribers',
            field=models.ManyToManyField(related_name='_accounts_user_subscribers_+', to=settings.AUTH_USER_MODEL, verbose_name='Subscribers'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='viewed_videos',
            field=models.ManyToManyField(related_name='viewed_by', to='videos.Video', verbose_name='Viewed videos'),
        ),
    ]
