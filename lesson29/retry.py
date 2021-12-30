import time
import requests


def constant_wait(sec):
    return lambda _: sec

no_wait = constant_wait(0)


def exponential_wait(attempt):
    return 2 ** attempt - 1


def retry(max_attempts=3, wait_fn=no_wait, ex_class_list=(Exception,)):
    def outer(fn):
        def inner(*args, **kwargs):
            ex = None
            for n in range(max_attempts):
                wait = wait_fn(n)
                print(f'Attempt {n}, delay: {wait}')
                try:
                    return fn(*args, **kwargs)
                except ex_class_list as e:
                    ex = e
                time.sleep(wait)
            raise ex
        return inner
    return outer


@retry(max_attempts=5, wait_fn=exponential_wait, ex_class_list=(requests.exceptions.HTTPError,))
def do_request():
    raise ValueError()
    res = requests.get('http://httpbin.org/status/404')
    res.raise_for_status()


do_request()
