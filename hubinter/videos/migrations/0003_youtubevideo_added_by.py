# Generated by Django 3.2.2 on 2021-07-13 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_youtubevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='added_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Added by'),
        ),
    ]
