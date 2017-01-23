a_string = "This is a global variable"

# Python functions create a new scope... 
# basically functions have their own namespaces



def foo():
	print a_string # Python first looks for a local variable 
				   # with this name. Since it cannot find it, 
				   # it looks for a global variable with 
				   # the same name


# Printing the builtin globals function returns a dictionary 
# containing all the variable names Python is aware of.

# print globals() # uncomment to see
foo()

