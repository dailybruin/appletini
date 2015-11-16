from prime.models import Issue, Article, PDF, Recipe, RecipeTag, DIYarticle, DIYTag, Neighborhood, CityGuideArticle, PrimeBase, PrimeArticle, PrimeCityGuide, PrimeRecipe, PrimeDIY
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import Http404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from itertools import chain
from django.db.models import Q

# utility functions

def get_recent_issues(issue_slug=None):
    if issue_slug is None:
        issue = Issue.objects.latest('release_date')
        recent_issues = Issue.objects.order_by('-release_date')[1:4]
    else:
        issue = get_object_or_404(Issue, slug=issue_slug)
        if issue == Issue.objects.latest('release_date'):
            recent_issues = Issue.objects.order_by('-release_date')[1:4]
        else:
            recent_issues = Issue.objects.order_by('-release_date')[0:3]
    return issue, recent_issues


# pages

class IssueView(View):
    def get(self, context, slug):
        issue, recent_issues = get_recent_issues(slug)

        diys = DIYarticle.objects.filter(issue=issue).order_by('position')
        recipes = Recipe.objects.filter(issue=issue).order_by('position')
        articles = Article.objects.filter(issue=issue).order_by('position')
        # result_list = list(chain(articles, recipes, diys))

        pdf = PDF.objects.get(issue=issue)
        context = {
            'issue': issue,
            'recent_issues': recent_issues,
            'articles': articles,
            'diys': diys,
            'recipes': recipes,
            'pdf': pdf,
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL
        }
        return render_to_response('prime/front.html', context)

class PastIssuesView(View):
    def get(self, context):
        current_issue, recent_issues = get_recent_issues()
        recent_issues = Issue.objects.order_by('-release_date')[1:]
        pdfs = []
        for issue in recent_issues:
            pdfs.append(PDF.objects.get(issue=issue))
        context = {
            'issue': current_issue,
            'recent_issues': recent_issues,
            'pdfs': pdfs,
            'hide_footer': True,
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL
        }
        return render_to_response('prime/past-issues-front.html', context)

class ArticleView(View):
    def get(self, context, issue_slug, article_slug):
        try:
            article = Article.objects.get(slug=article_slug)
        except Article.DoesNotExist:
            raise Http404
        if article.redirect:
            return redirect(article.redirect)
        articles = Article.objects.order_by('position')
        context = {
            'article': article,
            'articles': articles,
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL
        }
        return render_to_response('prime/article.html', context)



class LandingView(View):
    def get(self, context):
        current_issue, _ = get_recent_issues()
        article_list = Article.objects.order_by('position').reverse()
        paginator = Paginator(article_list, 10)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        context = {
            'current_issue': current_issue,
            'articles': articles,
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL
        }
        return render_to_response('prime/landing.html', context)

class CGView(View):
    def get(self, context):
        districts = Neighborhood.objects.all()
        context = {
            'districts': districts,
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/cityguide.html', context)

class DistrictView(View):
    def get(self, context, district_name):
        article_list = CityGuideArticle.objects.all();
        articles = article_list.filter(neighborhood__slug=district_name)
        see = articles.filter(option="see")
        do = articles.filter(option="do")
        eat = articles.filter(option="eat")
        neighborhood = Neighborhood.objects.get(slug=district_name)
        neighborhoods = Neighborhood.objects.all()[0:8]
        context = {
            'latest' : neighborhoods,
            'neighborhood': neighborhood,
            'see': see,
            'do': do,
            'eat': eat,
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/district.html', context)


class RecipeFrontView(View):
    def get(self, context):
        recipe_list = Recipe.objects.all()
        paginator = Paginator(recipe_list, 5)
        page = self.request.GET.get('page')
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)
        tags = RecipeTag.objects.all()
        context = {
            'articles': recipes,
            'tags': tags,
            'typeTitle': 'Recipes',
            'typeRoot': 'prime_recipe',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/diy-or-recipe-front.html', context)

class RecipeView(View):
    def get(self, context, issue_slug, recipe_slug):
        recipe = Recipe.objects.get(slug=recipe_slug)
        context = {
            'article': recipe,
            'typeTitle': 'Recipes',
            'typeRoot': 'prime_recipe',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/article.html', context)
    def get(self, context, recipe_slug):
        recipe = Recipe.objects.get(slug=recipe_slug)
        context = {
            'article': recipe,
            'typeTitle': 'Recipes',
            'typeRoot': 'prime_recipe',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/article.html', context)

class DIYView(View):
    def get(self, context, issue_slug, diy_slug):
        article = DIYarticle.objects.get(slug=diy_slug)
        context = {
            'article': article,
            'typeTitle': 'DIY',
            'typeRoot': 'prime_diy',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/article.html', context)
    def get(self, context, diy_slug):
        article = DIYarticle.objects.get(slug=diy_slug)
        context = {
            'article': article,
            'typeTitle': 'DIY',
            'typeRoot': 'prime_diy',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/article.html', context)

class RecipeTagsView(View):
    def get(self, context, tag_name):
        recipe_list = Recipe.objects.filter(tag__name=tag_name)
        paginator = Paginator(recipe_list, 15)
        page = self.request.GET.get('page')
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)
        tags = RecipeTag.objects.all()
        context = {
            'articles': recipes,
            'tags': tags,
            'tag_name': tag_name,
            'typeTitle': 'Recipes',
            'typeRoot': 'prime_recipe',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/diy-or-recipe-front.html', context)


class DIYFrontView(View):
    def get(self, context):
        diy_list = DIYarticle.objects.all()
        paginator = Paginator(diy_list, 5)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        tags = DIYTag.objects.all()
        context = {
            'articles': articles,
            'tags': tags,
            'typeTitle': 'DIY',
            'typeRoot': 'prime_diy',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/diy-or-recipe-front.html', context)

class DIYTagsView(View):
    def get(self, context, tag_name):
        diy_list = DIYarticle.objects.filter(tag__name=tag_name)
        paginator = Paginator(diy_list, 15)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        tags = DIYTag.objects.all()
        context = {
            'articles': articles,
            'tags': tags,
            'tag_name': tag_name,
            'typeTitle': 'DIY',
            'typeRoot': 'prime_diy',
            'STATIC_URL': settings.STATIC_URL,
            'MEDIA_URL': settings.MEDIA_URL
        }
        return render_to_response('prime/diy-or-recipe/diy-or-recipe-front.html', context)

class SearchResultView(View):
    def get(self, context):
        current_issue, _ = get_recent_issues()
        query = self.request.GET.get('query')
        article_list = PrimeBase.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        # article_list = Article.objects.order_by('position').reverse()
        paginator = Paginator(article_list, 10)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        context = {
            'current_issue': current_issue,
            'articles': articles,
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL
        }
        return render_to_response('prime/search.html', context)
# special handlers

def error404(request): # not currently implemented
    issue, recent_issues = get_recent_issues()
    print "hello"
    context = {
        'issue': issue,
        'recent_issues': recent_issues,
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL
    }
    return render_to_response('404.html', context)
