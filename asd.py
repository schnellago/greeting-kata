def keret():
	s= '*'
	n = 80
	result = ' '.join([char*n for char in s])
	return result

a = "Shasha"
def greeting(a):
	print(keret())
	print("Happy Eastern," + a)
	print(keret())
print(greeting(a))
