order = ['r','c','t','a']

# Converting order list to String
alphabet = ""
alphabet = alphabet.join(order)

l = []

# Accepting User input until null
while True:
      i = input("Enter string")
      if i == '':
            break
      l.append(i)

# Sorted based on key which is numeric value of each char assigned according to order
result = sorted(l, key=lambda word: [alphabet.index(c) for c in word])

print(result)
