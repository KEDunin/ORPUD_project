# Generated by Django 4.1.5 on 2023-05-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_analytics_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iphone',
            name='number',
        ),
        migrations.AlterField(
            model_name='iphone',
            name='memory',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='model',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
