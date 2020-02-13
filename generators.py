def generate_ints(n):
    for i in range(n):
        yield i

nested = [[1,2], [3,4], [5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

def flatten_recursive(nested):
    try:
        for sublist in nested:
            for element in flatten_recursive(sublist):
                yield element
                pass
    except TypeError:
        yield nested

def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(42)
print(next(r))
r.send("hello world!")
print(next(r))
