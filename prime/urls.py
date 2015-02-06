from django.conf.urls import patterns, url
from prime.views import IssueView, ArticleView, RecipeFrontView, DIYFrontView, LandingView, RecipeTagsView

urlpatterns = patterns('',
    url(r'^recipes/$', RecipeFrontView.as_view(), name='prime_recipe'),
    url(r'^recipes/tag/(?P<tag_name>\w+)/$', RecipeTagsView.as_view(), name='prime_recipe_tag'),
    url(r'^home/$', LandingView.as_view(), name='landing_view'),
    url(r'^diy/$', DIYFrontView.as_view(), name='prime_diy'),
    url(r'^(?P<slug>[-_\w]+)?/?$', IssueView.as_view(), name='prime_issue'),
    url(r'^(?P<issue_slug>[-_\w]+)/(?P<article_slug>[-_\w]+)/$', ArticleView.as_view(), name='prime_article'),
    # url(r'^cityguide/$', CityGuideFrontView.as_view(), name='prime_city'),
    # url(r'^recipes/(?P<recipe_slug>[-_\w]+)/$', RecipeView.as_view(), name='prime_recipes',
)
