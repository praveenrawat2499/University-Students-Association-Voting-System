# Generated by Django 3.1.7 on 2021-04-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_auto_20210415_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='course',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
