a_string = "This is a global variable"

def foo():
	a_string = "test" #This new local variable shadows the global var.
	print locals()

# foo()

print a_string
# print globals()