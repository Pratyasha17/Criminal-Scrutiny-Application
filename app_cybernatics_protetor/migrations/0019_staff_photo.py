# Generated by Django 3.0.5 on 2020-06-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0018_auto_20200624_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Photo',
            field=models.ImageField(default=None, upload_to='staff_image/'),
        ),
    ]
