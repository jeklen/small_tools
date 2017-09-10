# maybe the easiest way is using wget
# eg: wget -r http://web.stanford.edu/class/cs106b/
#  in this way, we can get all the file in the directory
from HTMLParser import HTMLParser
import urllib2
import os
import re

re_url = re.compile(r'^(([a-zA-Z]+)://([^/]+))(/.*)?$')

def resolve_link(link, url):
    m = re_url.match(link)
    if m is not None:
        if not m.group(4)
