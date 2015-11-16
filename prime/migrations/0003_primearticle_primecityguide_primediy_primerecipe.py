# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import prime.models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0002_auto_20151111_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeArticle',
            fields=[
                ('base_link', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('lead_photo', models.ImageField(upload_to=prime.models.CreateUploadPath(b'lead'))),
            ],
            bases=('prime.primebase',),
        ),
        migrations.CreateModel(
            name='PrimeCityGuide',
            fields=[
                ('base_link', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('option', models.CharField(max_length=256, choices=[(b'see', b'see'), (b'do', b'do'), (b'eat', b'eat')])),
                ('lead_photo', models.ImageField(upload_to=b'prime/cityguides/neighborhood/')),
                ('neighborhood', models.ForeignKey(to='prime.Neighborhood')),
            ],
            bases=('prime.primebase',),
        ),
        migrations.CreateModel(
            name='PrimeDIY',
            fields=[
                ('base_link', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('lead_photo', models.ImageField(upload_to=b'prime/diy/lead')),
                ('tag', models.ManyToManyField(to='prime.DIYTag')),
            ],
            bases=('prime.primebase',),
        ),
        migrations.CreateModel(
            name='PrimeRecipe',
            fields=[
                ('base_link', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('lead_photo', models.ImageField(upload_to=b'prime/recipe/lead')),
                ('tag', models.ManyToManyField(to='prime.RecipeTag')),
            ],
            bases=('prime.primebase',),
        ),
    ]
