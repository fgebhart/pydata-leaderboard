# Generated by Django 3.1.2 on 2020-11-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking_app', '0002_auto_20201101_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='user',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
