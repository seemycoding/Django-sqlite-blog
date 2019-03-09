# Generated by Django 2.1.5 on 2019-01-24 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('blog', '0003_auto_20190124_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=25)),
                ('body', models.CharField(max_length=255)),
            ],
        ),
    ]
