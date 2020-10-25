# Generated by Django 3.1.2 on 2020-10-25 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gradeit_app', '0002_auto_20201025_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('url', models.URLField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('technologies', models.CharField(blank=True, max_length=200)),
                ('cover_photo', pyuploadcare.dj.models.ImageField(blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['upload_date'],
            },
        ),
    ]