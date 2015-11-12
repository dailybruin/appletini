# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0006_auto_20151104_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primearticle',
            name='caption',
        ),
    ]
