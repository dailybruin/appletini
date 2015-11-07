# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import prime.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('prime', '0008_auto_20151104_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeCityGuide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(default=None, max_length=128)),
                ('teaser', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('authorDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('option', models.CharField(max_length=256, choices=[(b'see', b'see'), (b'do', b'do'), (b'eat', b'eat')])),
                ('lead_photo', models.ImageField(upload_to=b'prime/cityguides/neighborhood/')),
                ('author', models.ManyToManyField(to='main.Author')),
                ('issue', models.ForeignKey(default=None, blank=True, to='prime.Issue', null=True)),
                ('neighborhood', models.ForeignKey(to='prime.Neighborhood')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrimeDIY',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(default=None, max_length=128)),
                ('teaser', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('authorDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('lead_photo', models.ImageField(upload_to=b'prime/diy/lead')),
                ('author', models.ManyToManyField(to='main.Author')),
                ('issue', models.ForeignKey(default=None, blank=True, to='prime.Issue', null=True)),
                ('tag', models.ManyToManyField(to='prime.DIYTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrimeRecipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(default=None, max_length=128)),
                ('teaser', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('authorDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('lead_photo', models.ImageField(upload_to=b'prime/recipe/lead')),
                ('author', models.ManyToManyField(to='main.Author')),
                ('issue', models.ForeignKey(default=None, blank=True, to='prime.Issue', null=True)),
                ('tag', models.ManyToManyField(to='prime.RecipeTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='primearticle',
            name='article_type',
        ),
        migrations.AddField(
            model_name='primearticle',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='primearticle',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='primearticle',
            name='redirect',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='primearticle',
            name='slug',
            field=models.SlugField(default=None, max_length=128),
        ),
        migrations.RemoveField(
            model_name='primearticle',
            name='author',
        ),
        migrations.AddField(
            model_name='primearticle',
            name='author',
            field=models.ManyToManyField(to='main.Author'),
        ),
        migrations.AlterField(
            model_name='primearticle',
            name='lead_photo',
            field=models.ImageField(upload_to=prime.models.CreateUploadPath(b'lead')),
        ),
        migrations.AlterField(
            model_name='primearticle',
            name='teaser',
            field=models.TextField(blank=True),
        ),
    ]
