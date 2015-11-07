# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0011_auto_20151106_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primearticle',
            name='primebase_ptr',
        ),
        migrations.RemoveField(
            model_name='primebase',
            name='author',
        ),
        migrations.RemoveField(
            model_name='primebase',
            name='issue',
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
            name='PrimeBase',
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
