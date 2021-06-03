# Generated by Django 3.1 on 2021-03-19 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200928_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostpage',
            name='imported',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='blogpostpage',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
