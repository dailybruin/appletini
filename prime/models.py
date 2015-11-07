from django.db import models
from django.utils.text import slugify
from django.utils.deconstruct import deconstructible

from PIL import Image as PyImage

# utility functions

@deconstructible
class CreateUploadPath(object):

    def __init__(self, directory, same_model=False):
        self.same = same_model
        self.path = directory

    def __call__(self, instance, filename):
        if self.same:
            slug = instance.slug
        else:
            slug = instance.issue.slug
        return "prime/%(issue)s/%(directory)s/%(filename)s" %\
            {'issue': slug, 'directory': self.path,
             'filename': filename}

def getLatestIssue():
    return Issue.objects.latest('release_date')


# models

class Issue(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    release_date = models.DateField()
    get_upload_path = CreateUploadPath('header', same_model=True)
    header_image = models.ImageField(upload_to=get_upload_path, blank=True,
                                     null=True)

    class Meta:
        ordering = ['release_date']

    def __unicode__(self):
        return self.name

class Article(models.Model):
    issue = models.ForeignKey('Issue', default=None, null=True, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    get_upload_path = CreateUploadPath('lead')
    lead_photo = models.ImageField(upload_to=get_upload_path)
    teaser = models.TextField(blank=True)
    author = models.ManyToManyField('main.Author')
    body = models.TextField(blank=True)
    redirect = models.URLField(blank=True)
    position = models.PositiveIntegerField(default=0)

    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title

class Neighborhood(models.Model):
    lead_photo = models.ImageField(upload_to="prime/cityguides/lead")
    title = models.CharField(max_length=128, unique=True)
    intro_body = models.TextField(blank=True)
    slug = models.SlugField(max_length=128)
    def __unicode__(self):
        return self.title

class CityGuideArticle(models.Model):
    neighborhood = models.ForeignKey(Neighborhood)
    title = models.CharField(max_length=128)
    lead_photo = models.ImageField(upload_to="prime/cityguides/neighborhood/")
    option = models.CharField(max_length=256, choices=[('see', 'see'), ('do', 'do'), ('eat', 'eat')])
    body = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    issue = models.ForeignKey(Issue, blank=True, null=True)
    lead_photo = models.ImageField(upload_to="prime/recipe/lead")
    teaser = models.TextField(blank=True)
    author = models.ManyToManyField('main.Author')
    tag = models.ManyToManyField('RecipeTag')
    body = models.TextField(blank=True) #, widget=models.Field.Textarea(attrs={'rows': 40, 'cols': 120}))
    redirect = models.URLField(blank=True)
    position = models.PositiveIntegerField(default=0)

    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title

class DIYarticle(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    issue = models.ForeignKey(Issue, blank=True, null=True)
    lead_photo = models.ImageField(upload_to="prime/diy/lead")
    teaser = models.TextField(blank=True)
    author = models.ManyToManyField('main.Author')
    tag = models.ManyToManyField('DIYTag')
    body = models.TextField(blank=True) #, widget=models.Field.Textarea(attrs={'rows': 40, 'cols': 120}))
    redirect = models.URLField(blank=True)
    position = models.PositiveIntegerField(default=0)

    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title

class RecipeTag(models.Model):
    name = models.CharField(max_length = 32)

    def __unicode__(self):
        return "%s" % (self.name)

class DIYTag(models.Model):
    name = models.CharField(max_length = 32)

    def __unicode__(self):
        return "%s" % (self.name)


class Image(models.Model):
    get_upload_path = CreateUploadPath('article')
    image = models.ImageField(upload_to=get_upload_path)
    issue = models.ForeignKey('Issue', default=None, null=True, blank=True)
    author = models.ForeignKey('main.Author', null=True, blank=True)
    caption = models.TextField(blank=True)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.image != self.__original_image:
            size = 500, 1000
            super(Image, self).save(force_insert, force_update, *args, **kwargs)
            image = PyImage.open(self.image)
            image.thumbnail(size, PyImage.ANTIALIAS)
            image.save(self.image.path)
        else:
            super(Image, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_image = self.image

    def __unicode__(self):
        return "%s photo by %s (%s...)" % (self.issue, self.author,
                                           self.caption[0:50])

class PDF(models.Model):
    get_upload_path_pdf = CreateUploadPath('pdf')
    get_upload_path_pdf_image = CreateUploadPath('pdf_image')
    pdf = models.FileField(upload_to=get_upload_path_pdf)
    image = models.ImageField(upload_to=get_upload_path_pdf_image)
    issue = models.OneToOneField(Issue)

    def __unicode__(self):
        return "%s PDF" % self.issue


# class PrimeArticle(models.Model):
#     get_upload_path = CreateUploadPath('article')
#     ARTICLE = 'A'
#     CITYGUIDE = 'C'
#     DIYARTICLE = 'D'
#     RECIPE = 'R'
#     ARTICLE_TYPES = (
#         (ARTICLE, 'prime_article'),
#         (CITYGUIDE, 'city_guide'),
#         (DIYARTICLE, 'diy_article'),
#         (RECIPE, 'recipe'),
#     )
#     article_type = models.CharField(max_length=1, choices=ARTICLE_TYPES, default=ARTICLE)
#     title = models.CharField(max_length=128)
#     authorDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     issue = models.ForeignKey('Issue', default=None, null=True, blank=True)
#     author = models.ForeignKey('main.Author', null=True, blank=True)
#     lead_photo = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
#     teaser = models.TextField(null=True, blank=True)
#     # make ids for each different type of ARTICLE_TYPES
#
#     def getPrettyAuthors(self):
#         return ' and '.join([str(a) for a in self.author])
#
#     def __unicode__(self):
#         return self.title

class PrimeBase(models.Model):
    issue = models.ForeignKey('Issue', default=None, null=True, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, default=None)
    teaser = models.TextField(blank=True)
    author = models.ManyToManyField('main.Author')
    body = models.TextField(blank=True)
    redirect = models.URLField(blank=True)
    position = models.PositiveIntegerField(default=0)
    authorDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ARTICLE_TYPES = (
        ('ARTICLE', 'prime_article'),
        ('CITYGUIDE', 'prime_cityguide'),
        ('DIYARTICLE', 'prime_diy'),
        ('RECIPE', 'prime_recipe'),
    )
    article_type = models.CharField(max_length=1, choices=ARTICLE_TYPES)

    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title

class PrimeArticle(PrimeBase):
    get_upload_path = CreateUploadPath('lead')
    lead_photo = models.ImageField(upload_to=get_upload_path)
    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title


class PrimeCityGuide(PrimeBase):
    neighborhood = models.ForeignKey('Neighborhood')
    option = models.CharField(max_length=256, choices=[('see', 'see'), ('do', 'do'), ('eat', 'eat')])
    lead_photo = models.ImageField(upload_to="prime/cityguides/neighborhood/")

    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title

class PrimeRecipe(PrimeBase):
    lead_photo = models.ImageField(upload_to="prime/recipe/lead")
    tag = models.ManyToManyField('RecipeTag')

    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title

class PrimeDIY(PrimeBase):
    lead_photo = models.ImageField(upload_to="prime/diy/lead")
    tag = models.ManyToManyField('DIYTag')

    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title
