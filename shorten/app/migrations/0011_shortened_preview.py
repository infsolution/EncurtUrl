# Generated by Django 2.2 on 2019-04-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190426_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortened',
            name='preview',
            field=models.BooleanField(default=False),
        ),
    ]