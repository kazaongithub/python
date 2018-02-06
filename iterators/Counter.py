# Counter.py

class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Use this iterator in our code.
c1 = Counter(5, 10)
for i in c1:
    print(i, end = ' ')

print()

# The following example tries to show the code behind the scenes.
c2 = Counter(10, 15)
iterator = iter(c2)
while True:
    try:
        x = iterator.__next__()
        print(x, end=' ')
    except StopIteration as e:
        break
