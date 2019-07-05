def binarySearch (l, l, r, x): 

      # Base Case
      if r >= l: 

            mid = int(l + (r - l)/2)

            # Element present at the middle itself 
            if l[mid] == x: 
                  print("Element Found At Index", mid)

            # Element smaller than mid, find left subarray
            elif l[mid] > x: 
                  return binarySearch(l, l, mid-1, x) 

            # Element can only be present in right subarray
            else: 
                  return binarySearch(l, mid + 1, r, x)

      # Raising Exception
      else:
            raise Exception("Element Not Found")



# Test Array 
l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
x = 50

# Function Call
binarySearch(l, 0, len(l)-1, x)
