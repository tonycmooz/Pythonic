# PYTHON 2.7

# One clever way is to convert the string to a list first
name = raw_input("What is your name? ")
lst = list(name)

# Then reverse it
lst.reverse()

# And rejoin it
backwards = ''.join(lst)
print backwards

# But it is much much more Pythonic to do the following
name[::-1]
