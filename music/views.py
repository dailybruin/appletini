from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Album

class MainView(TemplateView):

    template_name = 'music/front.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.all()

        # Allow for clean rating star rending in the template:
        max_rating = 5
        for album in context['albums']:
            rating = album.rating
            if rating < 0:
                rating = 0
            elif rating > max_rating:
                rating = max_rating

            album.rating_range = xrange(rating)
            album.rating_range_alt = xrange(max_rating - rating)

        return context

