# Generated by Django 3.0.5 on 2020-06-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0017_auto_20200614_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Contact',
            field=models.IntegerField(unique=True),
        ),
    ]
