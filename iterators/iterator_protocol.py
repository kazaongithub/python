# iterator_protocol.py

class Seq:

    def __init__(self, max):
        self.x = 0
        self.max = max

    def __next__(self):
        self.x += 1

        if self.x > self.max:
            raise StopIteration

        return self.x ** self.x

    def __iter__(self):
        return self


s = Seq(10)
n = 0

for e in s:
    print(e)
