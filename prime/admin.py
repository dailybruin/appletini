from django.contrib import admin
from django.db import models
from django.forms import Textarea
from prime.models import Issue, Article, Image, PDF, Recipe, DIYarticle, CityGuideArticle, Neighborhood, RecipeTag, DIYTag

# admin.site.register(CityGuideArticle, CGAdmin)
class NeighborhoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Neighborhood, NeighborhoodAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Issue, IssueAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue', 'position')
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 40, 'cols': 120})
        },
    }
admin.site.register(Article, ArticleAdmin)

class CDAdmin(admin.ModelAdmin):
    Neighborhood = models.ForeignKey(Neighborhood)
admin.site.register(CityGuideArticle, CDAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    prepopulated_fields = {"slug": ("title",)}
    # formfield_overrides = {
    #     models.TextField: {
    #         'widget': Textarea(attrs={'rows': 40, 'cols': 120})
    #     },
    # }
admin.site.register(Recipe, RecipeAdmin)

class DIYAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(DIYarticle, DIYAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'caption', 'author', 'issue')
    readonly_fields = ('id',)
admin.site.register(Image, ImageAdmin)

class PDFAdmin(admin.ModelAdmin):
    list_display = ('issue', 'pdf')
admin.site.register(PDF, PDFAdmin)

class RecipeTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecipeTag)

class DIYTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(DIYTag)
