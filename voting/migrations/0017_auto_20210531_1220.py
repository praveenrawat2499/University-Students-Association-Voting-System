# Generated by Django 3.1.7 on 2021-05-31 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0016_auto_20210531_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='course_duration',
            new_name='year',
        ),
    ]
