from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # mainsite
    url(r'^', include('prime.urls')),
    # other apps
    url(r'^music/', include('music.urls'))
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
