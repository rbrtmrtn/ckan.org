# Generated by Django 3.1.1 on 2021-05-05 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0007_auto_20210420_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image'),
        ),
    ]