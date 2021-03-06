# Generated by Django 2.2 on 2019-04-20 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20190418_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortened',
            name='user',
        ),
        migrations.AddField(
            model_name='shortened',
            name='private_code',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_validated', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('contatos', models.ManyToManyField(to='app.Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='shortened',
            name='perfil',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shorteneds', to='app.Perfil'),
        ),
    ]
