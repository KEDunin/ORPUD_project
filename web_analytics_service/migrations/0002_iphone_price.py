# Generated by Django 4.1.5 on 2023-05-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_analytics_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iphone',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
