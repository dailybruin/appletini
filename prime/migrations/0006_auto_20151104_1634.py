# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0005_primearticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primearticle',
            name='authorDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
