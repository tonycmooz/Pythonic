# An example of a nested function

def outer():
	x = 1
	def inner():
		print x # Python looks for a local variable in the inner
	inner()		# then looks in the enclosing, outer

outer()			# Python looks in the scope of outer first
 				# and finds a local variable named inner


