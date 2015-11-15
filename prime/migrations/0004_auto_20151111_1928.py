# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0003_primearticle_primecityguide_primediy_primerecipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primearticle',
            name='base_link',
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
            name='base_link',
        ),
        migrations.RemoveField(
            model_name='primecityguide',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='primediy',
            name='base_link',
        ),
        migrations.RemoveField(
            model_name='primediy',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='primerecipe',
            name='base_link',
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
