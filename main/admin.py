from django.contrib import admin
from main.models import Author, RecipeTag, DIYTag

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author)

class RecipeTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecipeTag)

class DIYTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(DIYTag)
