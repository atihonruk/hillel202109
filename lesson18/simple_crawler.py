from urllib.parse import urljoin, urlsplit

import requests
import lxml.html


DOMAIN = 'https://docs.python.org'
NETLOC = urlsplit(DOMAIN).netloc
MAX_PAGES = 100

queue = [DOMAIN]
visited = set()  # enqueued
count_visited = 0

# <a href
# <img src=""

# with Session() as session:
while True:
    if count_visited > MAX_PAGES:
        break

    url = queue.pop()
    count_visited += 1
    res = requests.get(url)
    if res.status_code == requests.codes.ok:
        doc = lxml.html.fromstring(res.text)  # DOM tree, 50M / 200M
        for elem, attr, link, _ in doc.iterlinks():
            if elem.tag == 'a' and attr == 'href':
                link = urljoin(DOMAIN, link)  # make absolute
                if not urlsplit(link).netloc == NETLOC:
                    continue
                if link not in visited:
                    queue.append(link)
                    visited.add(link)

from pprint import pprint
pprint(visited)
        

    
