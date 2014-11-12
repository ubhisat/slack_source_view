__author__ = 'Satmeet'
from HTMLParser import HTMLParser
import logging

LOG = logging.getLogger(__name__)


class SlackHTMLParser(HTMLParser):
    """
    Class to override default HTMLParser implementation
    It will keep track of the tags in a dict as it parses
    the html text.
    Also it has a list, which would be used to reconstruct the
    original html content.
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.d = dict()
        self.content = []

    def handle_starttag(self, tag, attrs):
        # Increment the dictionary key value (for each tag)
        val = self.d.get(tag, 0)
        self.d[tag] = val + 1
        LOG.debug("%s - %s " % (tag, attrs))
        tag_str = self.mark_safe_start_tag_with_attrs(tag, attrs)
        self.content.append('<span class="%s">%s</span>' % (tag, tag_str))

    def handle_endtag(self, tag):
        self.content.append('<span class="%s">&lt;/%s&gt;</span>' % (tag, tag))

    def handle_data(self, data):
        self.content.append('<span>%s</span>' % (data))

    def mark_safe_start_tag_with_attrs(self, tag, attrs):
        if attrs:
            for kv in attrs:
                st = '%s="%s" ' % (kv[0], kv[1])

            return "&lt;%s %s&gt;" % (tag, st)
        return "&lt;%s&gt;" % tag
