# Generated by Django 3.1.7 on 2021-05-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0015_auto_20210531_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='year',
            new_name='course_duration',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='about',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]