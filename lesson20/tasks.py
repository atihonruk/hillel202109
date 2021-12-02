from celery import Celery


app = Celery('tasks',
             broker='redis://127.0.0.1/1',
             backend='redis://127.0.0.1/2')


# 5: 1 * 2 * 3 * 4 * 5 = 120
@app.task
def fac(n):
    for x in range(1, n):
        n *= x
    return n


# 1, 1, 2, 3, 5, 8
@app.task
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
