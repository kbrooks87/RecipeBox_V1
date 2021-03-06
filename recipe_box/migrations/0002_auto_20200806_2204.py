# Generated by Django 3.1 on 2020-08-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_box', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default='bio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='instructions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_required',
            field=models.CharField(default='time required', max_length=20),
            preserve_default=False,
        ),
    ]
