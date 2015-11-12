# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import prime.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('prime', '0004_delete_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_type', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'prime_article'), (b'C', b'city_guide'), (b'D', b'diy_article'), (b'N', b'neighborhood'), (b'R', b'recipe')])),
                ('title', models.CharField(max_length=128)),
                ('authorDate', models.DateTimeField(auto_now_add=True)),
                ('caption', models.TextField(null=True, blank=True)),
                ('lead_photo', models.ImageField(null=True, upload_to=prime.models.CreateUploadPath(b'article'), blank=True)),
                ('teaser', models.CharField(max_length=200, null=True, blank=True)),
                ('author', models.ForeignKey(blank=True, to='main.Author', null=True)),
                ('issue', models.ForeignKey(default=None, blank=True, to='prime.Issue', null=True)),
            ],
        ),
    ]
