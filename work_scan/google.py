import urllib2
import re

url = "https://www.google.com/?gfe_rd=cr&ei=aVj0VZLbG_DC8AeZlYHACA&gws_rd=ssl#q=xxx&start=0"

g_open = urllib2.urlopen(url)

xx = g_open.opener
print xx
