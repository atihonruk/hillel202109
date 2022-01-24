import sys
from typing import Iterable

# x! -> 1 .. x
# 5! -> 1 * 2 * 3 * 4 * 5

def fac(n: int) -> int:
    for i in range(1, n):
        n *= i
    return n

from functools import reduce
from operator import mul

def xfac(n: int) -> int:
    return reduce(mul, range(1, n+1), 1)

def rfac(a: int, n: int) -> int:
    assert n >= sys.getrecursionlimit(), 'Argument exceeds recursion limit'
    if n == 0:
        return a
    else:
        return rfac(a * n, n - 1)

test_nested = [1, [2, 3], 4, [5, (6, [7])]]

def flatten(seq: Iterable) -> Iterable:
    a = []
    for e in seq:
        if isinstance(e, (list, tuple)):
            a.extend(flatten(e))
        else:
            a.append(e)
    return a


def xflatten(seq: Iterable) -> Iterable:
    for e in seq:
        if type(e) is list:
            yield from xflatten(e)
        else:
            yield e

def validate_data(data):
    typedef = t.Dict({t.Key('message'): t.String}).allow_extra('*')
    typedef = t.Dict({t.Key('message'): t.String}).ignore_extra('*')
    
    # {'messag': 'hello, world'}    return typedef.check(data)

class Client:
    'Comand-line client'
    def cli():
        'cli function'
        print('Hello, python world')

            
if __name__ == '__main__':
    import fire

    fire.Fire(Client)

