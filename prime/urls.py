from django.conf.urls import patterns, url
from prime.views import DIYView, RecipeView, IssueView, ArticleView, RecipeFrontView, DIYFrontView, LandingView, RecipeTagsView, DIYTagsView

urlpatterns = patterns('',
<<<<<<< HEAD
	url(r'^recipes/$', RecipeFrontView.as_view(), name='prime_recipe'),
	url(r'^diy/$', DIYFrontView.as_view(), name='prime_diy'),
    url(r'^(?P<slug>[-_\w]+)?/?$', IssueView.as_view(), name='prime_issue'),
    url(r'^(?P<issue_slug>[-_\w]+)/(?P<article_slug>[-_\w]+)/$',
        ArticleView.as_view(), name='prime_article'),
=======
from prime.views import IssueView, ArticleView, RecipeFrontView, LandingView

urlpatterns = patterns('',
	url(r'^recipes/$', RecipeFrontView.as_view(), name='prime_recipe'),

	url(r'^home/$', LandingView.as_view(), name='landing_view'),
	# as landing view

<<<<<<< HEAD
    url(r'^(?P<slug>[-_\w]+)?/?$', IssueView.as_view(), name='prime_issue'),
     url(r'^(?P<issue_slug>[-_\w]+)/(?P<article_slug>[-_\w]+)/$',
         ArticleView.as_view(), name='prime_article'),
     url(r'^recipes/(?P<recipe_slug>[-_\w]+)/$', RecipeView.as_view(), name='prime_recipes',
=======
=======
    url(r'^recipes/$', RecipeFrontView.as_view(), name='prime_recipe'),
    url(r'^recipes/(?P<recipe_slug>[-_\w]+)/$', RecipeView.as_view(), name='prime_recipes'),
    url(r'^recipes/tagged/(?P<tag_name>[\w|\W]+)/$', RecipeTagsView.as_view(), name='prime_recipe_tag'),
    url(r'^diy/$', DIYFrontView.as_view(), name='prime_diy'),
    url(r'^diy/(?P<diy_slug>[-_\w]+)/$', DIYView.as_view(), name='prime_diys'),
    url(r'^diy/tagged/(?P<tag_name>[\w|\W]+)/$', DIYTagsView.as_view(), name='prime_diy_tag'),
    url(r'^home/$', LandingView.as_view(), name='landing_view'),
>>>>>>> 75b87d2ac47b5c559c8317eb06ee0d68d5ddb27b
    # url(r'^(?P<slug>[-_\w]+)?/?$', IssueView.as_view(), name='prime_issue'),
    # url(r'^(?P<issue_slug>[-_\w]+)/(?P<article_slug>[-_\w]+)/$', ArticleView.as_view(), name='prime_article'),
    # url(r'^cityguide/$', CityGuideFrontView.as_view(), name='prime_city'),
    # url(r'^recipes/(?P<recipe_slug>[-_\w]+)/$', RecipeView.as_view(), name='prime_recipes',
>>>>>>> 290c442a71444a37c02769795a645ea2faf7770b
)
