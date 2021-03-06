# Generated by Django 3.0.5 on 2020-06-08 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0003_createagent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='casecreation',
            name='file',
            field=models.FileField(default=None, upload_to='case_files/'),
        ),
        migrations.AddField(
            model_name='casecreation',
            name='image',
            field=models.ImageField(default=None, upload_to='case_image/'),
        ),
        migrations.AddField(
            model_name='casedetails',
            name='file',
            field=models.FileField(default=None, upload_to='case_files/'),
        ),
        migrations.AddField(
            model_name='casedetails',
            name='image',
            field=models.ImageField(default=None, upload_to='case_image/'),
        ),
    ]
