# Function to sort the list of tuples by its last item 
def sortTuple(tup):
	
	# Checking last element type for sorting
	char = tup[0][-1]

	# Handling Integer Last Element for sorting
	if char.isdigit():
		tup.sort(key = lambda x: int(x[-1].replace('\'','')))

	# Handling String Last Element (irrespective of case) for sorting
	else:
		tup.sort(key = lambda x: x[-1].lower())  

	return tup


# User Tuple Input
i = input("Enter List Of Tuples")

l = []

# Creating List of Tuples
for tup in i.split('),('):
	tup = tup.replace(')','').replace('(','')
	tup = tup.replace('\'','')
	l.append(tuple(tup.split(',')))

# Driver Code
print(sortTuple(l))


# Sample Test Cases
''' 

	('abcd','hi',5),('bacd','hi',10),('cabd','hi',9),('dacb','hi',20),('aabc','hi',6),('bacc','hi',18)
	(5,'hi','abcd'),(10,'hi','Bacd'),(9,'hi','cabd'),(20,'hi','dacb'),(6,'hi','Aabc'),(18,'hi','bacc')

'''