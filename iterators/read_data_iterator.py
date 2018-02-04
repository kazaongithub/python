# read_data_iterator.py

# The open() function returns a file object, which is an iterator.
# We can use it in a for loop.
# With the usage of an iterator, the code is cleaner.
with open('iterator.py', 'r') as f:
    for line in f:
        print(line.rstrip())
