# Generated by Django 3.2.2 on 2021-05-18 21:07

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('password', models.TextField(verbose_name='Password')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/%Y/%m', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg'])], verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Theme')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Video')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Video added')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Video updated')),
                ('preview', models.ImageField(blank=True, upload_to='previews/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg'])], verbose_name='Preview file')),
                ('video', models.FileField(upload_to='videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mov', 'mp4', 'mpeg4', 'avi', 'mpegps', 'flv'])], verbose_name='Video file')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='Dislikes')),
                ('comments_amount', models.IntegerField(default=0, verbose_name='Comments amount')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Tag')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tag added')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.theme', verbose_name='Relative theme')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Comment added')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Comment updated')),
                ('answer_for', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='videos.comment', verbose_name='Relative comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video', verbose_name='Video')),
            ],
        ),
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
            field=models.ManyToManyField(related_name='_videos_user_notifications_+', to=settings.AUTH_USER_MODEL, verbose_name='Notificatiosn'),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribers',
            field=models.ManyToManyField(related_name='_videos_user_subscribers_+', to=settings.AUTH_USER_MODEL, verbose_name='Subscribers'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
