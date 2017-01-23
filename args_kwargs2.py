# A value passed to a function (or method) when calling the function. 
# There are two kinds of argument:

# positional argument: an argument that is not a keyword argument. 
# Positional arguments can appear at the beginning of an argument list 
# and/or be passed as elements of an iterable preceded by *. For example, 
# 3 and 5 are both positional arguments in the following calls:

complex(3, 5)
complex(*(3, 5))

# keyword argument: an argument preceded by an identifier (e.g. name=) 
# in a function call or passed as a value in a dictionary preceded by **. 
# For example, 3 and 5 are both keyword arguments in the following calls 
# to complex():

complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})


# The single star * unpacks the sequence/collection into positional 
# arguments, so you can do this:

def sum(a, b):
    return a + b

values = (1, 2)

s = sum(*values)

# This will unpack the tuple so that it actually executes as:
# s = sum(1, 2)

print(s)

# The double star ** does the same, only using a dictionary 
# and thus named arguments:

values = { 'a': 1, 'b': 2 }
s = sum(**values)

print(s)


