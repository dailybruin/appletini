# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import prime.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('lead_photo', models.ImageField(upload_to=prime.models.CreateUploadPath(b'lead'))),
                ('teaser', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('author', models.ManyToManyField(to='main.Author')),
            ],
        ),
        migrations.CreateModel(
            name='CityGuideArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('lead_photo', models.ImageField(upload_to=b'prime/cityguides/neighborhood/')),
                ('option', models.CharField(max_length=256, choices=[(b'see', b'see'), (b'do', b'do'), (b'eat', b'eat')])),
                ('body', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DIYarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('lead_photo', models.ImageField(upload_to=b'prime/diy/lead')),
                ('teaser', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('author', models.ManyToManyField(to='main.Author')),
            ],
        ),
        migrations.CreateModel(
            name='DIYTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=prime.models.CreateUploadPath(b'article'))),
                ('caption', models.TextField(blank=True)),
                ('author', models.ForeignKey(blank=True, to='main.Author', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('release_date', models.DateField()),
                ('header_image', models.ImageField(null=True, upload_to=prime.models.CreateUploadPath(b'header', same_model=True), blank=True)),
            ],
            options={
                'ordering': ['release_date'],
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lead_photo', models.ImageField(upload_to=b'prime/cityguides/lead')),
                ('title', models.CharField(unique=True, max_length=128)),
                ('intro_body', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pdf', models.FileField(upload_to=prime.models.CreateUploadPath(b'pdf'))),
                ('image', models.ImageField(upload_to=prime.models.CreateUploadPath(b'pdf_image'))),
                ('issue', models.OneToOneField(to='prime.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('lead_photo', models.ImageField(upload_to=b'prime/recipe/lead')),
                ('teaser', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('author', models.ManyToManyField(to='main.Author')),
                ('issue', models.ForeignKey(blank=True, to='prime.Issue', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tag',
            field=models.ManyToManyField(to='prime.RecipeTag'),
        ),
        migrations.AddField(
            model_name='image',
            name='issue',
            field=models.ForeignKey(default=None, blank=True, to='prime.Issue', null=True),
        ),
        migrations.AddField(
            model_name='diyarticle',
            name='issue',
            field=models.ForeignKey(blank=True, to='prime.Issue', null=True),
        ),
        migrations.AddField(
            model_name='diyarticle',
            name='tag',
            field=models.ManyToManyField(to='prime.DIYTag'),
        ),
        migrations.AddField(
            model_name='cityguidearticle',
            name='neighborhood',
            field=models.ForeignKey(to='prime.Neighborhood'),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(default=None, blank=True, to='prime.Issue', null=True),
        ),
    ]
