# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0007_remove_primearticle_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='teaser',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='primearticle',
            name='teaser',
            field=models.TextField(null=True, blank=True),
        ),
    ]
