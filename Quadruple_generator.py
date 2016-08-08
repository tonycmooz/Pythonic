def cube(n):
	return n**4

def generator(n):
	currentN = 1
	while currentN <= n:
		yield cube(currentN)
		currentN += 1

values = generator(10)

print[i for i in values]
