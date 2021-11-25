from urllib.parse import urljoin, urlsplit
import asyncio


import aiohttp
import lxml.html

DOMAIN = 'https://docs.python.org'
NETLOC = urlsplit(DOMAIN).netloc
MAX_PAGES = 100

enqueued = set()
count_visited = 0


async def worker(session, queue):
    global count_visited

    while True:
        if count_visited >= MAX_PAGES:
            break
        count_visited += 1
        url = await queue.get()
        async with session.get(url) as res:
            if res.status != 200:
                continue
            try:
                txt = await res.text()  # socket.recv()
            except Exception as e:
                print(e)
                continue
            doc = lxml.html.fromstring(txt)  # DOM tree
            for elem, attr, link, _ in doc.iterlinks():
                if elem.tag == 'a' and attr == 'href':
                    link = urljoin(DOMAIN, link)  # make absolute
                    if not urlsplit(link).netloc == NETLOC:
                        continue
                    if link not in enqueued:
                        queue.put_nowait(link)
                        enqueued.add(link)


async def start():
    # session
    # queue
    async with aiohttp.ClientSession() as session:
        queue = asyncio.Queue()
        queue.put_nowait(DOMAIN)
        workers = [worker(session, queue) for n in range(10)]
        await asyncio.gather(*workers)


asyncio.run(start())
print(enqueued)

