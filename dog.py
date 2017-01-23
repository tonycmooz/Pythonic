class Dog():
	""" An attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in respone to a command."""
		print(self.name.title() + " rolled over!! Good boy! ")

my_dog = Dog('rocky', 1)



# print("My dog's name is " + my_dog.name.title() + ".")

print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()





