#### FROM : https://www.python.org/dev/peps/pep-0289/ ######

# Generator expressions are high performance, memory efficient generalization 
# of list comprehensions and generators. 

# We all know that list comprehensions are powerful and have widespread uses. 

# However many of the use cases do not need to have a full list created in 
# memory. Instead, they only need to iterate over the elements one at a time.

# Iterating over the generator expression or the list comprehension will do the 
# same thing. However, the list comprehension will create the entire list in 
# memory first while the generator expression will create the items on the fly, 
# so you are able to use it for very large (and also infinite!) sequences.

# If speed is crucial, use a list comprehension. 

# With big list comprehensions, you run out of memory
# With big generators, you run out of time


# Generator 
(x*2 for x in range(256))


# List comprehension
[x*2 for x in range(256)]


# For instance, the following summation code will build a full list of squares 
# in memory, iterate over those values, and, when the reference is no longer 
# needed, delete the list:

sum([x*x for x in range(10)])

# Memory is conserved by using a generator expression instead:

sum(x*x for x in range(10))


# Generator expressions are especially useful with functions like sum(), min(), 
# and max() that reduce an iterable input to a single value:

# max(len(line)  for line in file  if line.strip())

# Generator expressions also address some examples of functionals 
# coded with lambda:

# reduce(lambda s, a: s + a.myattr, data, 0)
# reduce(lambda s, a: s + a[3], data, 0)

# Which simplify to

# sum(a.myattr for a in data)
# sum(a[3] for a in data)

# Having a syntax similar to list comprehensions also makes it easy to convert 
# existing code into a generator expression when scaling up application.

# Early timings showed that generators had a significant performance advantage 
# over list comprehensions. However, the latter were highly optimized for Py2.4 
# and now the performance is roughly comparable for small to mid-sized data 
# sets. As the data volumes grow larger, generator expressions tend to perform
# better because they do not exhaust cache memory and they allow Python to 
# re-use objects between iterations.

# The semantics of a generator expression are equivalent to creating an anonymous 
# generator function and calling it. For example:

g = (x**2 for x in range(10))
print g.next()

# is equivalent to:

def __gen(exp):
    for x in exp:
        yield x**2
g = __gen(iter(range(10)))
print g.next()



# More on Generators
# PEP 255
# https://www.python.org/dev/peps/pep-0255/
