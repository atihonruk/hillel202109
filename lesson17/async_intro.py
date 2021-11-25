
def countdown(n):
    assert n > 0
    
    while n > 0:
        yield n  # BLOCKING
        n -= 1
    # raise StopIteration




    
# await



