# Generated by Django 3.1.7 on 2021-04-28 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0013_auto_20210428_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='sign',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]