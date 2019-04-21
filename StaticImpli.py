def counter(c):
    if c == 1:
        counter.cnt = 0
        return
    if 'cnt' not in counter.__dict__:
        counter.cnt = 0
    counter.cnt += 1
    return counter.cnt

