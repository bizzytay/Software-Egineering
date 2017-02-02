# git-exercise-01.py

# TEAM LEADER:
# implement this function so that it returns copy of string_arg reversed
def reverseWord(string_arg):
	return string_arg[::-1]

# TEAM MEMBER:
# implement this function so that it returns the frequency of query in string_arg
def countFreq(string_arg, query):
	frequency = 0
	for i in string_arg:
		if query == i:
			frequency = frequency + 1
	return frequency

<<<<<<< HEAD



def add(a,b):
	print "Adition: ",a + b

=======
def subtract(a, b):
	print "Sub", a - b
>>>>>>> c1fdbcc29e816631a7ce9f7bf8725edd366432ee

def main():
	data = 'guidorossumwashere'
	print 'REVERSED ==>', reverseWord(data)
	print 'FREQUENCY OF s IN', data, '==>', countFreq(data, 's')
<<<<<<< HEAD
	add(10,5)
=======
	subtract(1,5)
>>>>>>> c1fdbcc29e816631a7ce9f7bf8725edd366432ee

if __name__ == "__main__":
	main()
