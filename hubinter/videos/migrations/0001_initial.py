# Generated by Django 3.2.2 on 2021-06-28 12:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Tag')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tag added')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['theme'],
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Theme')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=300, unique=True, verbose_name='Slug')),
                ('description', models.TextField(max_length=2550, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Published')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('preview', models.ImageField(blank=True, default='C:\\Users\\Admin\\Desktop\\Python\\HubInter\\hubinter\\media/default_pictures/default_preview.png', upload_to='previews/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg', 'gmp'])], verbose_name='Preview file')),
                ('video', models.FileField(upload_to='videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mov', 'mp4', 'mpeg4', 'avi', 'mpegps', 'flv'])], verbose_name='Video file')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='Dislikes')),
                ('comments_amount', models.IntegerField(default=0, verbose_name='Comments')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('tags', models.ManyToManyField(related_name='videos', to='videos.Tag', verbose_name='Tags')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='videos.theme', verbose_name='Theme')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.theme', verbose_name='Theme'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('answer_for', models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to='videos.comment', verbose_name='Relative comment')),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('video', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='videos.video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-created_at'],
            },
        ),
    ]
