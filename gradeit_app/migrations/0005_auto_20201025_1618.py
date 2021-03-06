# Generated by Django 3.1.2 on 2020-10-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradeit_app', '0004_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.FloatField(blank=True),
        ),
    ]
