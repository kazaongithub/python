# iterator.py

# In Python a string is an immutable sequence of characters
str = 'formidable'

for e in str:
    print(e, end=" ")

print()

# The iter() function returns an iterator on object.
it = iter(str)

print(it.__next__())
print(it.__next__())
print(it.__next__())

print(list(it))