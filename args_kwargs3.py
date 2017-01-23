# One place where the use of *args and **kwargs 
# is quite useful is for subclassing.

class Foo():
	def __init__(self, value1, value2):
		# do something with the values
		print(value1, value2)

class MyFoo(Foo):
	"""docstring for ClassName"""
	def __init__(self, *arg, **kwargs):
		# do something ele, do not care about the args
		print('myFoo')
		super(MyFoo, self).__init__(*args, **kwargs)


# This way you can extend the behaviour of the Foo class, 
# without having to know too much about Foo. This can be quite 
# convenient if you are programming to an API which might change. 
# MyFoo just passes all arguments to the Foo class.
		
# An example where this could be used is in a situation where you 
# are providing an add-on for an existing product and want to
# override/extend some functionality. By using *args and **kwargs 
# this add-on will keep functioning if the underlying product 
# changes. However, instantiating MyFoo happens outside the add-on. 
# A decorator is a better example of when you can use *args and **kwargs.)
		
