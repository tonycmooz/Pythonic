# The *args and **kwargs is a common idiom to allow arbitrary number 
# of arguments to functions as described in the section more on defining 
# functions in the Python documentation.

# The syntax is the * and **. The names *args and **kwargs are only by 
# convention but there is no hard requirement to use them

# You would use *args when you are not sure how many arguments might be 
# passed to your function, i.e. it allows you to pass an arbitrary number
# of arguments to your function. For example:

def print_everything(*args):
	for count, thing in enumerate(args):
		print '{0}.{1}'.format(count, thing)

print_everything('apple', 'banana', 'cabbage')

print('\n')

# You can use **kwargs to let your functions take an arbitrary number of 
# keyword arguments ("kwargs" means "keyword arguments"):

def print_keyword_args(**kwargs):
	# kwargs is a dict of the keyword args passed to the function
	for key, value in kwargs.iteritems():
		print '{} = {}'.format(key, value)

kwargs = {'first_name': 'Tony', 'last_name': 'Mooz'}
print_keyword_args(**kwargs)
