# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0002_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='slug',
            field=models.SlugField(default=None, max_length=32),
        ),
    ]
