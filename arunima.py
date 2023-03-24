def common_data(list1, list2):
   result = False
   for x in list1:
      for y in list2:
         if x == y:
            result = True
            return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,3,4,5,6], [9,8,6,5]))

original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)




list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)


def common_data(list1, list2):
   result = False
   for x in list1:
      for y in list2:
         if x == y:
            result = True
            return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,3,4,5,6], [9,8,6,5]))


import itertools
my_list = [[1], [2, 3], [4, 5, 6, 7]]
flat_list = list(itertools.chain(*my_list))
print(flat_list)












