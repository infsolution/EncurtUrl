# Generated by Django 2.2 on 2019-04-21 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_perfil_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortened',
            name='perfil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shorteneds', to='app.Perfil'),
        ),
    ]