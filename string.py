# Python program to convert a list to string
	
# Function to convert
def listToString(s):
	
	# initialize an empty string
	str1 = ""
	
	# the string
	for i in s:
		str1 += i
	
	# return string
	return str1
			
s = ['code' , 'with' , 'tandora']
print(listToString(s))

