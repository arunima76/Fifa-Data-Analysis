test_list = [8,7,6,5,3,2,1]
res =[]
for i in test_list:
    if i not in res:
        res.append(i)
print("the list is removing duplicates", res)

l = []
if not l:
    print("List is not empty")

original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)

#Insert an element before each element of a list
color = ['Red','Blue','Green']
print("Original list", color)
color = [v for elt in color for v in ('c', elt)]
print("Original list", color)

#Write a Python program to insert an element before each element of a list.

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])


my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(my_list)


my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original_list")
print(my_list)
my_list.sort(key= lambda e: e['key']['subkey'], reverse = True)
print("Sorted List: ")
print(my_list)

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original_list")
print(my_list)
my_list.sort(key = lambda e: e['key']['subkey'], reverse = True)
print("Sorted List")
print(my_list)


my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original_list")
print(my_list)
my_list.sort(key = lambda e: e['key']['subkey'], reverse =True)
print("Sorted List")
print(my_list)

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])































	