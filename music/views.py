import json
import urllib
import urllib2

from math import ceil, floor

from django.http import HttpResponse

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

            album.rating_range = xrange(int(floor(rating)))
            album.rating_range_alt = xrange(max_rating - int(ceil(rating)))

            album.need_half_star = True
            if (abs(rating - floor(rating)) < 0.1): # 0.1 acts as "epsilon"
                album.need_half_star = False

        return context

def fetch_review(request):
    review_url = request.GET['url']
    post_data = [('json', '1')]
    req = urllib2.Request(review_url, urllib.urlencode(post_data))

    opener = urllib2.build_opener()
    opener.addheaders = [('Accept-Charset', 'utf-8')]
    response = opener.open(req)
    data = response.read().decode('utf-8')

    # Only grab the content field of the JSON response.
    # (This has to be done manually, and as a string, because the JSON response from DB is corrupted in some way)
    content = ''
    beginning = data.index('"content"') + len('"content"') + 2
    for i in xrange(beginning, len(data)):
        # End on '",':
        if (data[i] == '"' and data[i + 1] == ','):
            break
        content += data[i]

    # Now strip out '\'s and '\n's:
    cleaned_content = ''
    i = 0
    while i < len(content):
        if content[i] == '\\':
            if content[i + 1] == 'n':
                i += 1
        else:
            cleaned_content += content[i]

        i += 1

    json_response = {}
    json_response['content'] = cleaned_content

    return HttpResponse(json.dumps(json_response), content_type='application/json')
