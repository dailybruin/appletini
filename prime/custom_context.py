from prime.models import Issue, Article, PDF, Recipe, DIYarticle, Neighborhood, CityGuideArticle
from main.models import RecipeTag, DIYTag
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import Http404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


def get_base_content(request):
    footer = Article.objects.get(pk=1)
    return {"footer" : footer}