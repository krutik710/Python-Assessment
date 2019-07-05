pairs = []

# Accepting Input Until Null
while True:
	i = input()
	if i is '':
		break
	pairs.append(i)


d = {}
count = 0


# Filling individual names in dict with value showing association
for i in pairs:
	n1 = i.split()[0]
	n2 = i.split()[1]

	# If first name exists in dict, insert second name with same value as first
	if n1 in d:
		val = d[n1]
		d[n2] = val

	# If second name exists in dict, insert first name with same value as second
	elif n2 in d:
		val = d[n2]
		d[n1] = val

	# If no name exists in dict, insert them and assign value of count
	else:
		d[n1] = count
		d[n2] = count
		count+=1



# result = []

# # Creating list of names having same value in dict
# for i in range(count):
# 	result.append([k for k,v in d.items() if v == i ])

# Part One Result
print(count)


# Part 2 input, single pair of names
pair = input("Enter Pair To Check Association")
n1 = pair.split()[0]
n2 = pair.split()[1]
v1 = d[n1]
v2 = d[n2]

# If value is same for both words in dict, then they are associated
if v1 == v2:
	print("YES")
else:
	print("NO")