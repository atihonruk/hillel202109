import asyncio
from threading import Thread
from threading import Lock


_counter = 0

def incr():
    global _counter

    for _ in range(1000):
        for _ in range(1000):
            _counter += 1


def show_counter():
    threads = [Thread(target=incr) for _ in range(10)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
        print(t.getName() + ' finished')
    
    print(_counter)



def task(n):
    for x in range(10):
        for y in range(10):
            print(f'Thread {n}: {x} {y}')


def run_threads():
    t1 = Thread(target=task, args=(1,))
    t2 = Thread(target=task, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


async def atask(n):
    for x in range(10):
        await asyncio.sleep(0.001)
        for y in range(10):
            print(f'Coro {n}: {x} {y}')



def run_coros():
    async def main():
        await asyncio.gather(atask(1), atask(2))

    asyncio.run(main())



