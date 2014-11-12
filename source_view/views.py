from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
import requests
from .utils import SlackHTMLParser
import logging

LOG = logging.getLogger(__name__)


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        rc = RequestContext(request)
        return render(request, self.template_name, context_instance=rc)

    def post(self, request, *args, **kwargs):
        rc = RequestContext(request)
        url = request.POST.get('url')
        try:
            # Add http:// to the url if not provided
            if not (url.startswith('http://') or url.startswith('https://')):
                url = "http://%s" % url

            # Fetch the html using the request library
            r = requests.get(url)
            source = r.text
            LOG.debug(source)

            # Use the parser
            sp = SlackHTMLParser()
            sp.feed(source)
            items = dict()
            items['tags'] = sp.d.copy()
            items['source'] = '\r\n'.join(sp.content)
            items['url'] = url
            return render(request, 'source.html', items, context_instance=rc)
        except Exception as e:
            LOG.error(str(e))
            return render(request, self.template_name, {'error': 'Bad Request',
                                                        'error_detail': str(e)},
                          context_instance=rc)

