# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('organization', models.CharField(default=b'Daily Bruin', max_length=32, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('twitter', models.CharField(max_length=15, blank=True)),
                ('facebook', models.CharField(max_length=32, blank=True)),
                ('mug', models.ImageField(null=True, upload_to=b'mug/%Y', blank=True)),
                ('bio', models.TextField(blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
