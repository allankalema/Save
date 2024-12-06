# Generated by Django 5.1.3 on 2024-12-06 10:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Useractivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('comments', models.PositiveBigIntegerField(blank=True, default=True, null=True)),
                ('likes', models.PositiveBigIntegerField(blank=True, default=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
