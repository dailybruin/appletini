# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0009_auto_20151106_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primearticle',
            name='author',
        ),
        migrations.RemoveField(
            model_name='primearticle',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='primecityguide',
            name='author',
        ),
        migrations.RemoveField(
            model_name='primecityguide',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='primecityguide',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='primediy',
            name='author',
        ),
        migrations.RemoveField(
            model_name='primediy',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='primediy',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='primerecipe',
            name='author',
        ),
        migrations.RemoveField(
            model_name='primerecipe',
            name='issue',
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
