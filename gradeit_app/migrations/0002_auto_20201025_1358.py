# Generated by Django 3.1.2 on 2020-10-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradeit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
