# Generated by Django 2.2 on 2019-04-18 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortened',
            name='url_shortened',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
