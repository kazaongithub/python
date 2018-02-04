# read_data.py

# This code prints the contents of the file
# It uses a while loop
with open('iterator.py', 'r') as f:
    while True:
        line = f.readline()

        if not line:
            break
        else:
            print(line.rstrip())