# Generated by Django 2.2.5 on 2019-09-28 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190730_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortened',
            options={'ordering': ('-id',)},
        ),
    ]