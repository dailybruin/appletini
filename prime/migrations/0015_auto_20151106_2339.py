# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0014_auto_20151106_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primearticle',
            name='primebase_ptr',
        ),
        migrations.RemoveField(
            model_name='primecityguide',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='primecityguide',
            name='primebase_ptr',
        ),
        migrations.RemoveField(
            model_name='primediy',
            name='primebase_ptr',
        ),
        migrations.RemoveField(
            model_name='primediy',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='primerecipe',
            name='primebase_ptr',
        ),
        migrations.RemoveField(
            model_name='primerecipe',
            name='tag',
        ),
        migrations.DeleteModel(
            name='PrimeArticle',
        ),
        migrations.DeleteModel(
            name='PrimeCityGuide',
        ),
        migrations.DeleteModel(
            name='PrimeDIY',
        ),
        migrations.DeleteModel(
            name='PrimeRecipe',
        ),
    ]
