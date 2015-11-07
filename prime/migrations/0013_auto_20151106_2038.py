# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import prime.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('prime', '0012_auto_20151106_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(default=None, max_length=128)),
                ('teaser', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('authorDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('article_type', models.CharField(max_length=1, choices=[(b'ARTICLE', b'prime_article'), (b'CITYGUIDE', b'prime_cityguide'), (b'DIYARTICLE', b'prime_diy'), (b'RECIPE', b'prime_recipe')])),
            ],
        ),
        migrations.CreateModel(
            name='PrimeArticle',
            fields=[
                ('primebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('lead_photo', models.ImageField(upload_to=prime.models.CreateUploadPath(b'lead'))),
            ],
            bases=('prime.primebase',),
        ),
        migrations.CreateModel(
            name='PrimeCityGuide',
            fields=[
                ('primebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('option', models.CharField(max_length=256, choices=[(b'see', b'see'), (b'do', b'do'), (b'eat', b'eat')])),
                ('lead_photo', models.ImageField(upload_to=b'prime/cityguides/neighborhood/')),
                ('neighborhood', models.ForeignKey(to='prime.Neighborhood')),
            ],
            bases=('prime.primebase',),
        ),
        migrations.CreateModel(
            name='PrimeDIY',
            fields=[
                ('primebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('lead_photo', models.ImageField(upload_to=b'prime/diy/lead')),
                ('tag', models.ManyToManyField(to='prime.DIYTag')),
            ],
            bases=('prime.primebase',),
        ),
        migrations.CreateModel(
            name='PrimeRecipe',
            fields=[
                ('primebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='prime.PrimeBase')),
                ('lead_photo', models.ImageField(upload_to=b'prime/recipe/lead')),
                ('tag', models.ManyToManyField(to='prime.RecipeTag')),
            ],
            bases=('prime.primebase',),
        ),
        migrations.AddField(
            model_name='primebase',
            name='author',
            field=models.ManyToManyField(to='main.Author'),
        ),
        migrations.AddField(
            model_name='primebase',
            name='issue',
            field=models.ForeignKey(default=None, blank=True, to='prime.Issue', null=True),
        ),
    ]
