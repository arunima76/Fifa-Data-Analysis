def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr

list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))


from collections import Counter
 
 
def checkInFirst(a, b):
     # getting count
    count_a = Counter(a)
    count_b = Counter(b)
 
    # checking if element exists in second list
    for key in count_b:
        if key not in count_a:
            return False
        if count_b[key] > count_b[key]:
            return False
    return True
 
 
# initializing list
a = [1, 2, 4, 5]
b = [1, 2, 3]
 
# Calling function
res = checkInFirst(a, b)
 
# Printing list
print("Original list : " + str(a))
print("Original sub list : " + str(b))
 
if res == True:
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")
 
def checkInFirst(a,b):
     count_a = Counter(a)
     count_b = Counter(b)

     for key in count_b:
          if key not in count_a:
               return False
          if count_b[key] > count_b[key]:
               return False
        return True



