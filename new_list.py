#Newlist
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

#Write a Python program to get unique values from a list

my_list = [10,90,20,50,60]
print("Original list")
my_list2 = list(my_list)
print("Original list", my_list)

#Write a python program to get a unique values from a list
import collections
my_list = [10,10,20,60,90,30,50]
print("Original List is", my_list)
ctr = collections.Counter(my_list)
print("The element is" ,ctr)


#Write a Python program to count the number of elements in a list within a specified range

def count_range_list(li, min, max):
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr

list1 = [10,20,40,50,10,20,40,100,500]
print(count_range_list( list1, 40, 100))
list2 = ['a','b','c','d','e']
print(count_range_list(list2, 'a','e'))  

#Python propgramme to remove the dictionary 

test_list = [8,7,6,5,3,2,1]
res = []
for i in test_list:
  if i not in res:
      res.append(i)
print("the list is removing duplicates", res)


#Python check if a list exists in another list


list = [[1,5,7], [2,3,4],[3,6,9],[4,8,12]]
check_list =[2,3,4]
if check_list in list:
    print("List is present")
else:
    print("List is not present")



fruits1 = ['Mango','Orange','Apple','Jackfruit']
fruits2 = ['Mango', 'Orange','Apple','Jackfruit']
new_list = all(item in fruits1 for item in fruits2)

if new_list is True:
    print("True")
else:
    print("Flase")



#Python chcek if a value exist in a list of lists 

nested_list = [[2,4,6,8,12,14,16], [3,6,9,12,15],[4,8,12,16,20,24]]
value1 = 8
value2 = 0

result1 = value1 in (item for sublist in nested_list for item in sublist)
result2 = value2 in (item for sublist in nested_list for item in sublist)

print(result1), "\n", (result2)


def common_data(list1, list2):
   result = False
   for x in list1:
      for y in list2:
         if x == y:
            result = True
            return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,3,4,5,6], [9,8,6,5]))


list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)


from itertools import chain
list = [[5,10,15,20,25], [10,20,30,40], [25,50,75,90]]
element_serach1 = 40
element_search2 = 50

result1 =  element_serach1 in chain(*list) 
result2 = element_search2 in chain(*list) 

print((result1), "\n", (result2))

# printing the tuples in object directly

l1 = ["eat","sleep","repeat"]

for ele in enumerate(l1):
    print(ele)
for count, ele in enumerate(l1,100 ):
    print(count)
    print(ele)


list1 = [[2,4,6,8,10],[1,3,5,7,9],[4,8,12,16,20]]
search_item = 16
if search_item in(item for sublist in list1 for item in sublist):

     print("Elemnt is present")
else:
   print("Element Not Present")

from itertools import chain
list = [[5,10,15,20,25], [10,20,30,40], [25,50,75,90]]
element_search1 = 40
result1 = element_search1 in chain(*list)
result2 = element_search2 in chain(*list)
print((result1), "\n", (result2)) 

nested_list = [[2,4,6,8], [3,6,9], [4,8,12]] 
element = 3
result = element in (element for sublist in nested_list for element in sublist) 
print((result))


list = [["watermelon"], ["mango"], ["orange"], ["apple"]] 
check_list = ["orange"]
if check_list in list: 
	print("List is present") 
else: 
	print("List is not present")
        
        
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)


my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)


chocolate = ["5star", "silk", "milkybar"]
newchocolate_list = [a for a in chocolate if "5" in a]
print(newchocolate_list)


cube = lambda a: a * a * a
print(cube(5))

number = [5,10,15,20,25,30,35,40,45,50]
newnumber = list(map(lambda c: c/5 ,number))
print(newnumber)


num = [i for i in range(10) if i>=5]
print(num)


num = [i for i in range(50) if i%2==0 if i%3==0 if i%3==0]
print(num)

num = [i for i in range(30) if i>=2 if i<=25 if i%4==0 if i%8==0]
print(num)


fruits = ["mango" if i%3==0 else "orange" for i in range(10)]
print(fruits)

for i in range(2,4):
        for j in range(1,5):
               print(f"{i}+{j}={i+j}")


list = [[2,4,6,8]]
matrix = [[row[i] for row in list] for i in range(4)]
print(matrix)


country_list = ['USA', 'United Kingdom', 'Canada']

# Assign the first element of the list to a variable
first_item = country_list[0]

# Print the value of the variable to the console
print(first_site)



country_list = ['USA', 'United Kingdom', 'Canada', 'Brazil']
# Create a new list that contains elements from index 1 up to (but not including) index 3 of the original list
sub_list = country_list[1:3]
# Print the new list to the console
print(sub_list)
# Create a list of numbers
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create a new list that contains only the even numbers from the original list using a lambda function and the filter() method
even_list = list(filter(lambda x: x % 2 == 0, num_list))
# Print the new list to the console
print(even_list)


# import the random module
import random
# create a list of countries
country_list = ['USA', 'United Kingdom', 'Canada', 'Brazil']
# select a random country
random_country = random.choice(country_list)
print('A randomly selected country is:', random_country)


#Insert an item at end of a list in Python using append() function
list_name.insert(index, value)
usa_st_gdp = [8.6, 8.5, 7.8, 7.1]
print(usa_st_gdp)
usa_st_gdp.insert(len(usa_st_gdp), 6.9)
usa_st_gdp = [8.6, 8.5, 7.8, 7.1]
print(usa_st_gdp)






















