import urllib2
import re

f = open('tags.txt', 'w')
url_base = 'https://ctftime.org/tasks/?page='
max_page = 286
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
expr = re.escape('<span class="label label-info">') + r'.*'  + re.escape('</span>')
tags = {}

for i in range(1, max_page+1):
    url = url_base + str(i)
    req = urllib2.Request(url, headers=hdr)
    page = urllib2.urlopen(req)
    content = page.read()
    html_tags = re.findall(expr, content)
    for t in html_tags:
        t = t.replace('<span class="label label-info">', '').replace('</span>', '')
        tags[t] = tags.get(t, 0) + 1

for key, value in sorted(tags.items(), key=lambda item: item[1], reverse=True):
    f.write(key+" "+str(value)+"\n")
        
f.close()
