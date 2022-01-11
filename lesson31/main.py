import sys

## Debugging
a, b = 0, 1
print(f'{a} {b}', file=sys.stderr)

# breakpoint()
# - For python < 3.4:
# import pdb; pdb.set_trace()

  
## Measuring relative execution time: timeit


# x! -> 1 .. x
# 5! -> 1 * 2 * 3 * 4 * 5

def fac(n):
    for i in range(1, n):
        n *= i
    return n

from functools import reduce
from operator import mul

def xfac(n):
    return reduce(mul, range(1, n+1), 1)

def rfac(a, n):
    assert n >= sys.getrecursionlimit(), 'Argument exceeds recursion limit'
    if n == 0:
        return a
    else:
        return rfac(a * n, n - 1)


import timeit

print('fac: ', timeit.timeit(lambda: fac(100)))
print('xfac: ', timeit.timeit(lambda: xfac(100)))
    


## Recursion, recursion limit

test_nested = [1, [2, 3], 4, [5, (6, [7])]]

def flatten(seq):
    a = []
    for e in seq:
        if isinstance(e, (list, tuple)):
            a.extend(flatten(e))
        else:
            a.append(e)
    return a


def xflatten(seq):
    for e in seq:
        if type(e) is list:
            yield from xflatten(e)
        else:
            yield e

##  augmented assigment

t = (1, [2, 3])
# t[1] += [4, 5]

## Disassembling: dis

from dis import dis
dis('t[1] += [4, 5]')


## operator chaining
5 in range(10) == True
dis('5 in range(10) == True')


## bytes vs str

with open(__file__, 'rb') as f:
    assert type(f.read()) is bytes

with open(__file__, 'rt') as f:
    assert type(f.read()) is str

# str.encode()
# bytes.decode()
  
## float vs Decimal
#! 3.51234 == 3.51234
# math.isclose
