# Generated by Django 3.0.5 on 2020-06-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0007_auto_20200611_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Contact',
            field=models.IntegerField(),
        ),
    ]
