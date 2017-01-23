# Function parameters can be either positional parameters
# that are mandatory or named 
# Or default valye parameters that are optional.


def foo(x, y=0): # (positional parameter, named param.)
	print x - y

foo(3, 1) # both arguments are positional

foo(3) # uses the named parameter by default

# foo() # no first (mandatory/positional) parameter raises an Error


foo(y=1, x=3)

# Python supports named arguments at function call time. Here I am
# calling a function with two named arguments even though it was 
# defined with one named and one positional parameter. Since I have 
# names for my parameters the order I pass them in does not matter




