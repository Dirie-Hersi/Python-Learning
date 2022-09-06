def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step
        

generator = gen_range(10)
print(next(generator))



