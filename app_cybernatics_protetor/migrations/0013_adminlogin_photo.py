# Generated by Django 3.0.5 on 2020-06-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0012_auto_20200612_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminlogin',
            name='photo',
            field=models.ImageField(default=None, upload_to='admin_image/'),
        ),
    ]