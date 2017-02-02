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

def subtract(a, b):
	print "Sub", a - b

def main():
	data = 'guidorossumwashere'
	print 'REVERSED ==>', reverseWord(data)
	print 'FREQUENCY OF s IN', data, '==>', countFreq(data, 's')
	subtract(1,5)

if __name__ == "__main__": 
	main()
