# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0013_auto_20151106_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primebase',
            name='article_type',
            field=models.CharField(max_length=10, choices=[(b'ARTICLE', b'prime_article'), (b'CITYGUIDE', b'prime_cityguide'), (b'DIYARTICLE', b'prime_diy'), (b'RECIPE', b'prime_recipe')]),
        ),
    ]
