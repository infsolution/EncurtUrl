# Generated by Django 2.2 on 2019-04-21 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190421_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortened',
            name='code',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]
