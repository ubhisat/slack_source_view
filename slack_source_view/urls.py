from django.conf.urls import patterns, include, url
import source_view.urls as source_urls
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', include(source_urls)),
    # url(r'^admin/', include(admin.site.urls)),
)

